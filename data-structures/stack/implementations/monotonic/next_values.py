def get_next_smallest_mono_increase_stack(arr):
    stack = []
    next_smallest = [-1 for _ in range(len(arr))]
    
    for right in range(len(arr)):
        while stack and arr[stack[-1]] > arr[right]:
            index = stack.pop()
            next_smallest[index] = right
        stack.append(right)  
    return next_smallest

def get_greater_element_mono_deacrease(arr):
    stack = []
    next_largest = [-1 for _ in range(len(arr))]
    
    for right in range(len(arr)):
        while stack and arr[stack[-1]] < arr[right]:
            next_largest[stack.pop()] = right
        stack.append(right)
    return next_largest



test_1 = [9, 16, 25, 4, 1]
test_2 = [5, 23, 20, 14, 2, 17, 11, 8]
test_3 = [3, 12, 7, 7]


print(get_greater_element_mono_deacrease(test_1))
print(get_greater_element_mono_deacrease(test_3))
print(get_greater_element_mono_deacrease(test_2))

 