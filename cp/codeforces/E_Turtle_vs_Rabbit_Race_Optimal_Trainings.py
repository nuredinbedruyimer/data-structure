from bisect import bisect_left, bisect_right


def get_value(sections, intial):
    return ((intial + (intial - sections + 1)) * (sections))// 2




test = int(input())


for _ in range(test):
    n = int(input())
    
    arr = list(map(int, input().split()))
    arr = [0] + arr
    prefix_sum = [arr[0]]
    
    for i in range(1, n + 1):
        prefix_sum.append(prefix_sum[-1] + arr[i])
    
    
    
    queries = int(input())
    ans_list = []
    
    for _ in range(queries):
        left, u = list(map(int, input().split()))
        
        low = left
        high = n
        
        ans = left
        
        while low <= high:
            middle = (low + high)// 2
            curr_value = prefix_sum[middle] - prefix_sum[left - 1]
            if curr_value <= u:
                ans = max(ans, middle)
                low = middle + 1
            else:
                high = middle - 1
        left_boundary = max(left, ans)
        right_boundary = min(n, ans + 1) + 1
        max_gain = float("-inf")
        index = -1
        for valid_index in range(left_boundary, right_boundary):
            sections = prefix_sum[valid_index] - prefix_sum[left - 1]
            curr = get_value(sections, u)
            
            if curr > max_gain:
                max_gain = curr
                index = valid_index
        ans_list.append(index)
    print(*ans_list)
            
        

    
        
            
        
        
        
        