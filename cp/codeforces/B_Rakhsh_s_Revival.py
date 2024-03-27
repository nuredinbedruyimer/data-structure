test = int(input())

for _ in range(test):
    n, m, k = list(map(int, input().split()))
    word = list(input())
    
    right = 0
    left = 0
    ans = 0
    
    while right < n:
        if word[right:right + m].count("0") == m:
            ans += 1
            right += m + k - 1
        else:
            right += m
    print(ans)
            
    