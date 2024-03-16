def find_first_index_v1(arr, target):
    low = 0
    
    high = len(arr) - 1
    
    ans = 0
    
    
    while low <= high:
        middle = (low + high )// 2
        if arr[middle] == target:
            ans = middle 
            high = middle - 1
        elif arr[middle] > target:
            high = middle - 1
        else:
            low = middle + 1
    return ans

def find_first_index_v2(arr, target):
    low = 0
    high = len(arr)
    while high > low + 1:
        middle = (high + low)//2
        if arr[middle] >= target:
            high = middle
        else:
            low = middle
    return low

if __name__ == "__main__":
    arr = list(map(int, input().split()))
    target = int(input())
    
    print("First Occure At : ", find_first_index_v2(arr, target))
    