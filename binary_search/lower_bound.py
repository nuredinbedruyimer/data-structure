def lower_bound(arr, target):
    low = 0
    high = len(arr) -1
    
    
    while high > low + 1:
        mid = (low + high) // 2
        if arr[mid] >= target:
            high = mid
        else:
            low = mid + 1
    if arr[low] >= target:
        return low
    elif arr[high] >= target:
        return high
    else:
        return len(arr)




if __name__ == "__main__":
    input("Enter Sorted List Of Number >> ")
    arr = list(map(int, input().split()))
    
    target = int(input())
    
    print("Lower Bound : ", lower_bound(arr, target))