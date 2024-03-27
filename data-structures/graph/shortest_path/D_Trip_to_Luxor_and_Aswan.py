


def black_box(window, arr, target):
    for i in range(len(arr)):
        arr[i] += (i + 1) * window
    
    #  find the max window with 
    
    left = 0
    curr_sum = 0
    arr.sort()
    
    for a in arr:
        curr_sum += a
        if curr_sum > target:
            break
        left += 1
    return left >= window, curr_sum


n, k = list(map(int, input().split()))
arr = list(map(int, input().split()))

low = 0

high = n
ans = 0

while low <= high:
    middle = (low + high) // 2
    
    if black_box(middle, arr[:], k)[0]:
        ans = middle
        _, cost = black_box(middle, arr[:], k)
        low  = middle + 1
    else:
        high = middle - 1
cost = 0       
for i in range(len(arr)):
    arr[i] += (i + 1) * ans
arr.sort()

for i in range(min(ans, n)):
    cost += arr[i]
print(ans, cost)



