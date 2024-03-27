n, k = list(map(int, input().split()))
arr = list(map(int, input().split()))

left = 0
count = 0
ans = 1

for right in range(1,n):
    if arr[right] != arr[right - 1]:
        ans = max(ans, right - left + 1)
    else:
        left = right
print(ans)
    