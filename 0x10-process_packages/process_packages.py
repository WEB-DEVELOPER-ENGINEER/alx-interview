def process_packets(buffer_size, packets):
    buffer = []
    start_times = []
    current_time = 0
    for arrival_time, process_time in packets:
        while buffer and buffer[0] <= arrival_time:
            buffer.pop(0)
        if len(buffer) >= buffer_size:
            start_times.append(-1)
        else:
            start_time = max(current_time, arrival_time)
            start_times.append(start_time)
            buffer.append(start_time + process_time)
            current_time = start_time + process_time
    return start_times

def main():
    buffer_size, n = map(int, input().split())
    packets = [tuple(map(int, input().split())) for _ in range(n)]
    start_times = process_packets(buffer_size, packets)
    for start_time in start_times:
        print(start_time)

if __name__ == "__main__":
    main()