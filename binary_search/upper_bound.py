def upper_bound(arr, target):
    low = 0
    high = len(arr) - 1
    while low < high - 1:
        middle = (low + high) // 2
        
        if arr[middle] > target:
            high = middle
        else:
            low = middle
    ans = 0
    if arr[high] >= target:
        ans =  high
    elif arr[low] >= target:
        ans =  low
    if arr[-1] < target:
        ans = len(arr)
    return ans



if __name__ == "__main__":
    arr = list(map(int, input().split()))
    target = int(input())
    
    print("Upper Bound : ", upper_bound(arr, target))