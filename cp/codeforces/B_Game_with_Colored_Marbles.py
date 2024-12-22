from collections import defaultdict

test = int(input())
for _ in range(test):
    n = int(input())
    arr = list(map(int, input().split()))
    memo = defaultdict(int)
    
    for a in arr:
        memo[a] += 1
    alice_part = (n // 2) + n % 2
    
    
    uniques = 0
    non_uniques = 0
    
    for key in memo.keys():
        if memo[key] == 1:
            uniques += 1
        else:
            non_uniques += 1
    alices = (uniques // 2) + uniques % 2
    alices *= 2
    alices += non_uniques 
    
    print(alices)
    
    