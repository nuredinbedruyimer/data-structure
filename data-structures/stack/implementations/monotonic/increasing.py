def mono_increase_stack(arr):
    stack = []
    
    for right in range(len(arr)):
        while stack and arr[stack[-1]] > arr[right]:
            stack.pop()
        stack.append(right)
        
    return stack


test_1 = [9, 16, 25, 4, 1]
test_2 = [5, 23, 20, 14, 2, 17, 11, 8]
test_3 = [3, 12, 7]


print(mono_increase_stack(test_1))
print(mono_increase_stack(test_3))
print(mono_increase_stack(test_2))

def mono_decrease_stack(arr):
    stack = []
    
    for right in range(len(arr)):
        while stack and arr[stack[-1]] < arr[right]:
            stack.pop()
        stack.append(right)
    return stack
        
        
print(mono_decrease_stack(test_1))
print(mono_decrease_stack(test_3))
print(mono_decrease_stack(test_2))
