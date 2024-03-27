a, c = list(map(int, input().split()))


def ternary(n):
    t = [0 for _ in range(30)]
    index = 29
    
    while n > 0:
        t[index] = n % 3
        index -= 1
        n //= 3 
    return t

def get_value(b):
    ans = 0
    index = 0
    while b:
        value = b.pop()
        
        ans += value *( 3 ** index)
        index += 1

    return ans



a_t = ternary(a)
c_t = ternary(c)


b_t = []



for i in range(30):

    if c_t[i] == 0:
        if a_t[i] == 1:
            b_t.append(2)
        elif a_t[i] == 2:
            b_t.append(1)
        elif a_t[i] == 0:
            b_t.append(0)
    elif c_t[i] == 1:
        if a_t[i] == 1:
            b_t.append(0)
        elif a_t[i] == 2:
            b_t.append(2)
        elif a_t[i] == 0:
            b_t.append(1)
    elif c_t[i] == 2:
        if a_t[i] == 1:
            b_t.append(1)
        elif a_t[i] == 2:
            b_t.append(0)
        elif a_t[i] == 0:
            b_t.append(2)

print(get_value(b_t))


        
