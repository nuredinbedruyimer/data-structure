def solve(arr, target):
    n = len(arr)
    left = 0
    minimum_window = n
    min_window_start = 0
    curr_sum = 0
    for right in range(n):
        curr_sum += arr[right]
        while left <= right and curr_sum >= target :
            curr_sum -= arr[left]
            if right - left + 1 < minimum_window:
                min_window_start = left 
                minimum_window = right - left + 1
            left += 1
    return [min_window_start + 1, minimum_window]



n, target = list(map(int, input().split()))
arr = list(map(int, input().split()))
total = sum(arr)
arr = arr + arr




add = (target // total) * n
target -= (target // total) * total



window, start =  solve(arr, target)
print(window, start + add)