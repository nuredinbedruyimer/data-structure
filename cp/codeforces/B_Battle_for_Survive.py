test = int(input())

for _ in range(test):
    n = int(input())
    
    arr = list(map(int, input().split()))
    
    
    ans = arr[-1] - (arr[-2] - sum(arr[:-2]))
    
    print(ans)