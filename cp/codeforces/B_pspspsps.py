test = int(input())

for _ in range(test):
    length = int(input())
    chars = list(input())
    chars[-1] = "." if chars[-1] == 'p' else chars[-1]
    chars[0] = "." if chars[0] == 's' else chars[0]
    
    is_s_found = is_p_found  = 0
    
    for i in chars:
        if i == "p":
            is_p_found += 1
        if i == "s":
            is_s_found += 1
    if is_s_found and is_p_found :
        print("NO")
    else:
        print("YES")
    