def get_answer():
        n, k = map(int, input().split())
        monsters_health = list(map(int, input().split()))
        monsters_position = list(map(int, input().split()))
        temp= [0 for _ in range(n+1)]
        for i in range(n):
            temp[abs(monsters_position[i])]+=monsters_health[i]
        potential = k
        flag = False
        for i in range(1,n+1):
            if potential<temp[i]:
                flag = True
                break
            potential-=temp[i]
            potential+=k
        if flag:
             print("NO")
 
        else:
             print("YES")
 
test = int(input())
for _ in range(test):
     get_answer()
 