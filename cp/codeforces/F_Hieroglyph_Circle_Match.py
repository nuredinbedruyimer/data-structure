from collections import defaultdict

SIZE = 2000010
memo = [0 for _ in range(SIZE)]
vis = defaultdict(lambda: -1)

la, lb = map(int, input().split())
arr = list(map(int, input().split()))
brr = list(map(int, input().split()))

for i in range(1, lb + 1):
    vis[brr[i - 1]] = i

max_length = 0
window_start, window_end = 1, 0

for i in range(1, 2 * la + 1):
    pos = vis[arr[(i - 1) % la]]

    if pos == -1:
        window_start, window_end = 1, 0
    else:
        if window_start <= window_end and pos <= memo[window_end]:
            pos += ((memo[window_end] - pos + lb) // lb) * lb

        window_end += 1
        memo[window_end] = pos

        while window_start <= window_end and pos - memo[window_start] >= lb:
            window_start += 1

    max_length = max(max_length, window_end - window_start + 1)

print(max_length)

