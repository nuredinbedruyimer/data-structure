def get_next_smallest_mono_increase_stack(arr):
    stack = []
    next_smallest = [-1 for _ in range(len(arr))]
    
    for right in range(len(arr)):
        while stack and arr[stack[-1]] > arr[right]:
            index = stack.pop()
            next_smallest[index] = right
        stack.append(right)  
    return next_smallest

def next_greater_value(arr):
    stack = []
    next_largest = [len(arr) for _ in range(len(arr))]
    
    for right in range(len(arr)):
        while stack and arr[stack[-1]] < arr[right]:
            next_largest[stack.pop()] = right
        stack.append(right)
    return next_largest

def prev_greater_value(arr):
    stack = []
    prev_max = [-1 for _ in range(len(arr))]
    for right in range(len(arr) - 1, -1, -1):
        while stack and arr[stack[-1]] < arr[right]:
            index = stack.pop()
            prev_max[index] = right
        stack.append(right)
    return prev_max


test_1 = [9, 16, 25, 4, 1]
test_2 = [5, 23, 20, 14, 2, 17, 11, 8]
test_3 = [3, 12, 7, 7]
test_4 =  [3]

def sum_of_max_of_subarray(arr):
    prev_max = prev_greater_value(arr)
    next_max = next_greater_value(arr)
    ans = 0
    
    for idx in range(len(arr)):
        right = next_max[idx] - idx
        
        left = idx - prev_max[idx]
        print(left, right)
        
        ans += right * left * arr[idx]
    return ans


print(sum_of_max_of_subarray(test_4))
# print(sum_of_max_of_subarray(test_3))
# print(sum_of_max_of_subarray(test_2))

 