test = int(input())

for _ in range(test):
    n , k = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    
    arr.sort(reverse=True)
    
    alice = 0 
    bob = 0
    
    
    
    
    for i in range(1, n, 2):
        need = arr[i - 1] - arr[i]
        alice += arr[i - 1]
        if k >= 0:
            bob += arr[i] + min(k, need)
            k -= min(k, need)
        else:
            bob += arr[i]
    if n % 2 == 1:
        alice += arr[-1]
        


    print(alice - bob)
        