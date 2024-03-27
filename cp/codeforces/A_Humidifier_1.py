n = int(input())

arr = []

for _ in range(n):
    a, b = list(map(int, input().split()))
    arr.append([a, b])


volume_so_far = arr[0][1] 
for i in range(1, n):
    volume_so_far  = max(volume_so_far- (arr[i][0] - arr[i - 1][0]), 0)
    volume_so_far += arr[i][1]


print(volume_so_far)
    