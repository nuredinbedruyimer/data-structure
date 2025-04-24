def get_answer():
    password = list(input())
    n = int(input())
    first = False
    second = False
    for i in range(n):
        temp = list(input())
        if temp == password:
            return "YES"
        if temp[0] == password[1]:
            second = True
        if temp[1] == password[0]:
            first = True
    
    if first and second:
        return "YES"
    else:
        return "NO"
        
print(get_answer())