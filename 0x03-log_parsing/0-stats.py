#!/usr/bin/python3
import re
import sys
import signal

ip_address_pattern = r'(\b25[0-5]|\b2[0-4][0-9]|\b[01]?[0-9][0-9]?)(\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3}'
allowed_status_codes = (200, 301, 400, 401, 403, 404, 405, 500)
status_code_pattern = '|'.join(map(str, allowed_status_codes))
log_entry_pattern = fr'^{ip_address_pattern} - \[[^\]]+\] "GET /projects/\d+ HTTP/1\.1" ({status_code_pattern}) (\d+)$'
line_count = 0
total_size = 0
status_code_counts = {str(code): 0 for code in allowed_status_codes}
def print_statistics():
    print(f"File size: {total_size}")
    for code, count in sorted(status_code_counts.items()):
        if count > 0:
            print(f"{code}: {count}")
def handle_interrupt(signum, frame):
    print_statistics()
    sys.exit(0)
signal.signal(signal.SIGINT, handle_interrupt)
try:
    for line in sys.stdin:
        line = line.strip()
        line_count += 1
        match = re.match(log_entry_pattern, line)
        if match:
            status_code = int(match.group(4))
            file_size = int(match.group(5))
            total_size += file_size
            if status_code in allowed_status_codes:
                status_code_counts[str(status_code)] += 1
        if line_count == 10:
            print_statistics()
            line_count = 0
finally:
    print_statistics()
