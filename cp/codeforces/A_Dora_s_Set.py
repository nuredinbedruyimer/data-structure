test = int(input())


for _ in range(test):
    l, r = list(map(int, input().split()))
    ans = 0
    
    for i in range(l, r + 1):
        ans += i % 2 == 1
    print(ans//2)