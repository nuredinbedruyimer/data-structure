
INF = float("inf")
test = int(input())

for _ in range(test):
    num_a, _ = map(int, input().split())
    arr = list(map(int, input().split()))
    m = int(input())
    arr.insert(0, -INF)
    num_a += 1
    
    for i in range(1, num_a):
        if arr[i] < arr[i - 1] and m - arr[i] < arr[i - 1]:
            continue
        arr[i] = min(INF if arr[i] < arr[i - 1] else arr[i], INF if m - arr[i] < arr[i - 1] else m - arr[i])
    
    print("YES" if all(arr[i] >= arr[i - 1] for i in range(1, num_a)) else "NO")