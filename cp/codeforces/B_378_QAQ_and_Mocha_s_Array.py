test = int(input())
for _ in range(test):
    n = int(input())
    ans = "No"
    
    arr = list(map(int, input().split()))
    arr = list(set(arr))
    if len(arr) <= 2:
        print("Yes")
    else:
        arr.sort()
        first_min_element , second_min_element = arr[0], arr[1]
        

        for d in [first_min_element, second_min_element]:
            for i in range(n):
                if arr[i] != -1 and arr[i] % d == 0 :
                    arr[i] = -1
        if len(arr) == arr.count(-1):
            print("Yes")
        else:
            print("No")