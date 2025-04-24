test = int(input())


for _ in range(test):
    arr = list(map(int, input().split()))
    arr.insert(2, -1)
    ans = 0
    value = -1
    
    for i in range(402):
        arr[2] = i - 201
        count = 0
        for i in range(2, len(arr)):
            if arr[i - 1] + arr[i - 2] == arr[i]:
                count += 1
        if count > ans:
            ans = count
            value = i
    print(ans)