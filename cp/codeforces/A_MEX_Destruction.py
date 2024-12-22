test = int(input())

for _ in range(test):
    n = int(input())
    arr = list(map(int, input().split()))
    right = 0
    memo = []
    temp = []
    left = 0
    
    while right < n :
        if arr[right] > 0:
            temp.append(arr[right])
        else:
            if temp:
                memo.append(temp[:])
                temp = []
        right += 1
    if temp:
        memo.append(temp)
    print(min(len(memo), 2))
            
        

   