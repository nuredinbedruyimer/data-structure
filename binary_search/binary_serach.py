def binary_search_v1(arr, target):
    low = 0
    high = len(arr) - 1
    
    
    while low <= high:
        middle = (low + high) // 2
        if arr[middle] == target:
            return middle
        elif arr[middle] > target:
            high = middle - 1
        else:
            low = middle + 1
    return -1


if __name__ == "__main__":
    input("Please Enter Sorted List Of Element 'Press Enter To Start Entering Number'")
    arr = sorted(list(map(int, input().split())))
    
    target = int(input())
    
    if binary_search_v1(arr, target) == -1:
        print("Element not Found !!")
    else:
        print("Element Found At : ", binary_search_v1(arr, target), " Index")