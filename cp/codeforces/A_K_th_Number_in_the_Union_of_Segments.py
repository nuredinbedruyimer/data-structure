n , k = list(map(int, input().split()))


def helper(low, high, target):
    if low <= target <= high:
        return target - low + 1
    elif high < target:
        return high - low + 1
    else:
        return 0
    


ranges = []

for _ in range(n):
    left, right = list(map(int, input().split()))
    ranges.append([left, right])
    

    
low = -int(2e9)
high = int(2e9)

ans = -1

while low <= high:
    target = (low + high) // 2
    count = 0
    for i in range(n):
        count += helper(ranges[i][0], ranges[i][1], target)
    if count >=  k + 1:
        ans = target
        high = target - 1
    else:
        low = target + 1
print(ans)
        
    