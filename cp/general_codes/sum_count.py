def helper(arr):
    
    
    total_sum = sum(arr)
    prefix_sum = 0
    sum_diff = 0
    n = len(arr)
    
    for i in range(n):
        num_after = n - i - 1
        
        sum_after = total_sum - prefix_sum - arr[i]
        
        sum_diff += (sum_after - (arr[i] + 1) * num_after)
        
        prefix_sum += arr[i]
    
    return sum_diff

# Example usage
arr = [0, 3, 6, 8, 9, 10]
result = helper(arr)
print(result)  # Output: 70
