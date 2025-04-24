test = int(input())
for _ in range(test):
    n, left , right = list(map(int, input().split())) 
    
    
    arr = list(map(int, input().split())) 
    
    left -= 1
    right -= 1
    
    min_value = float("inf")
    max_value = float("-inf")
    
    
    for index in range(left, right + 1):
        min_value = min(min_value, arr[index])
        max_value = max(max_value, arr[index])
        
    
    right_part = []
    
    left_part = []
    
    
    for i in range(right + 1,n ):
        if arr[i] <= max_value:
            right_part.append(arr[i])
    for  i in range(0, left):
        if arr[i] <= max_value:
            left_part.append(arr[i])
    left_part.sort()
    
    right_part.sort()
    
    temp = sorted(arr[left : right + 1])
    
    opt1 = sum(temp)
    
    for i in range(len(left_part)):
        if temp and temp[-1] >= left_part[i]:
            element = temp.pop()
            opt1 -= element
            opt1 += left_part[i]
    temp = sorted(arr[left : right + 1])
    
    opt2 = sum(temp)
    for i in range(len(right_part)):
        if temp and temp[-1] >= right_part[i]:
            element = temp.pop()
            opt2 -= element
            opt2 += right_part[i]
    
    
    
    print(min(opt2, opt1))