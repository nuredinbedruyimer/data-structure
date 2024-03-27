test = int(input())


for _ in range(test):
    arr = list(map(int, input().split()))
    arr.sort()
    
    area = min(arr[0], arr[1]) * min(arr[-1], arr[-2])
    print(area)