n, k = list(map(int, input().split()))

def get_index(arr, value):
    for i in range(len(arr)):
        if arr[i] == value:
            return i
    return -1

arr = list(map(int, input().split()))
brr = list(map(int, input().split()))


is_found = False
if len(brr) == 1:
    arr[get_index(arr, 0)] = brr[0]
    if list(sorted(arr)) == arr:
        print("No")
        is_found = True
if not is_found:
    print("Yes")
