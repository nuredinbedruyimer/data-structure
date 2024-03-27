test = int(input())

for _ in range(test):
    n = int(input())
    arr = list(map(int, input().split()))
    word = input()
    
    
    prefix_sum = [0]
    for a in arr:
        prefix_sum.append(prefix_sum[-1] + a)
    
    
    left = 0
    right = n - 1
    ans = 0
    
    while left <= right:
        if word[left] == "L" and word[right] == "R":
            ans += prefix_sum[right + 1] - prefix_sum[left]
            left += 1
            right -= 1
        elif word[right] == "L" and word[left] == "R":
            left += 1
            right -= 1
        elif word[left] == "R":
            left += 1
        else:
            right -= 1
            
    
    print(ans)
            
    
            
            
            