def max_sliding_window(sequence, m):
    max_values = []
    window = []
    for i in range(m):
        while window and sequence[i] >= sequence[window[-1]]:
            window.pop()
        window.append(i)
    for i in range(m, len(sequence)):
        max_values.append(sequence[window[0]])
        while window and window[0] == i - m:
            window.pop(0)
        while window and sequence[i] >= sequence[window[-1]]:
            window.pop()
        window.append(i)
    max_values.append(sequence[window[0]])
    return max_values

def main():
    n = int(input())
    sequence = list(map(int, input().split()))
    m = int(input())
    max_values = max_sliding_window(sequence, m)
    print(' '.join(map(str, max_values)))

if __name__ == "__main__":
    main()