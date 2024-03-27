test = int(input())


for _ in range(test):
    s1 = input()
    s2 = input()
    
    n1 = len(s1)
    n2 = len(s2)
    ans = n1  + n2
    
    is_found = False
    if s1[0] != s2[0]:
        
        is_found = True
    else:
        ans += 1
        for i in range(min(n1, n2)):
            if s1[i] != s2[i]:
                break
            if s1[i] == s2[i]:
                ans -= 1
    print(ans)
    