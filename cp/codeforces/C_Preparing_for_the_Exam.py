test = int(input())

for _ in range(test):
    n, m, k = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    brr = list(map(int, input().split()))
    not_answered = set()
    answer = set(brr)
    ans = []
    all_q = list(range(1, n + 1))
    seen = set(all_q)
    for a in all_q:
        if a not in answer:
            not_answered.add(a)  
    if len(not_answered) >= 2:
        ans = [False for _ in range(n)]
    
    else:
        for i in range(m):
            
            seen.remove[all_q[i]]
            for a in list(not_answered):
                if a in seen:
                    ans.append(False)
                else:
                    ans.append(True)
            seen.add(all_q[i])
                
                    
            
        
    print(not_answered)    
            