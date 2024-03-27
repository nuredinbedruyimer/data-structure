n, k = list(map(int, input().split()))
arr = list(map(int, input().split()))

ans = 2

for i in range(1, n):
    if arr[i] - arr[i - 1] > 2 * k:
        ans += 2
    elif arr[i] - arr[i-1] == 2 * k:
        ans += 1
print(ans)