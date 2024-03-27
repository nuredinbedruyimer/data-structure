test = int(input())

for _ in range(test):
    word = input()
    text = input()
    
    W = len(word)
    T = len(text)
    t_pointer = 0
    
    ans = list(word)
    
    for i in range(W):
        if (t_pointer < T and word[i] == "?") or (t_pointer < T and word[i] == text[t_pointer]):
            
            ans[i] = text[t_pointer]
            t_pointer += 1
            
    if t_pointer == T:
        for i in range(W):
            if ans[i] == "?":
                ans[i] = "z"
        print("YES")
        print("".join(ans))
    else:
        print("NO")
            