test = int(input())

def solve(alice_interval, bob_interval):


    if max(alice_interval[0], bob_interval[0]) <= min(alice_interval[1], bob_interval[1]):
        if alice_interval[0] == bob_interval[0]:
            
            return min(alice_interval[1], bob_interval[1]) - max(alice_interval[0], bob_interval[0]) + 1
        if alice_interval[1] == bob_interval[1]:
            return min(alice_interval[1], bob_interval[1]) - max(alice_interval[0], bob_interval[0]) + 1
        return min(alice_interval[1], bob_interval[1]) - max(alice_interval[0], bob_interval[0]) + 2
    else:
        return 1


for _ in range(test):
    l, r = list(map(int, input().split()))
    L, R = list(map(int, input().split()))
    
    ans = solve([l, r], [L, R])
    print(ans)
    