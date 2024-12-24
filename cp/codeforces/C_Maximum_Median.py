n, k = list(map(int, input().split()))

arr = list(map(int, input().split()))


def black_box(arr, median, k):
    count = 0
    for a in arr:
        count += abs(a - median) if a <= median else 0
        
    return count <= k
    
        
    


arr.sort()


middle = len(arr) // 2

temp = arr[middle:]

low = arr[0]
high = arr[-1] + k


while high >= low :
    mid = (low + high) // 2
    if black_box(temp, mid, k):

        ans = mid
        low = mid + 1
    else:
        high = mid - 1
        
print(ans)








