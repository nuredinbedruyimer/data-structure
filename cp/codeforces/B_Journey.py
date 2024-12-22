test = int(input())

for _ in range(test):
    n, a, b, c = list(map(int, input().split()))
    
    total = a + b + c
    days = n // total
    days *= 3
    
    remain = n % total
    temp = [a, b, c]
    curr = 0
    
    
    for i in range(len(temp)):
        if remain <= 0:
            break
        if remain - temp[i] <= 0:
            
            days = days + i + 1
            break
        remain -= temp[i]
    print(days)
        