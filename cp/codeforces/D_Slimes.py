from bisect import bisect_right


def get_prefix(arr):
    n = len(arr)
    prefix_sum = [0 for _  in range(n + 1)]
    for i in range(1, n + 1):
        prefix_sum[i] = prefix_sum[i - 1] + arr[i - 1]
    return prefix_sum
def solve(arr):
    n = len(arr)
        
    prefix_sum = get_prefix(arr)
    
    last_change = [-1 for _ in range(n)]
    ans = [n for _ in range(n)]
    
    #  start from left and find the avvlue which eat the current value after it start from the left come from the right
    
    for index in range(1, n):
        low = 1
        high = index
        
        #  find the number of element or window size we picke from left side
        while low <= high:
            window = (low + high) // 2
            if prefix_sum[index] - prefix_sum[index - window] > arr[index] and  last_change[index - 1] >= index - window:
                ans[index] = min(ans[index], window)
                high =  window - 1
            else:
                low = window + 1
        # if the addecent element are in different form 
        
        if arr[index - 1] > arr[index]:
            ans[index] = 1
        last_change[index] = last_change[index - 1] if arr[index] == arr[index - 1] else index - 1 
    return ans
        



test = int(input())

for _ in range(test):
    n = int(input())
    
    arr = list(map(int, input().split()))
    max_value = float("inf")
    ans = [-1 for _ in range(n)]
    ans1 = solve(arr)
    ans2 = solve(arr[::-1])[::-1]
    
    for i in range(n):
        if min(ans1[i], ans2[i]) == n:
            continue
        else:
            ans[i] = min(ans1[i], ans2[i])
    print(*ans)
    
    

        
        
    

    