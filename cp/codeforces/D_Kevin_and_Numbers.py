from heapq import heapify, heappop, heappush

def can_transform(n, m, arr, brr):
    # If sums are not equal, transformation is impossible
    if sum(arr) != sum(brr):
        return "NO"
    
    # Sort array A
    arr.sort()
    
    # Convert array B to a max-heap (negate values for min-heap behavior)
    brr = [-x for x in brr]
    heapify(brr)
    
    # Process until all elements of arr are matched
    while arr:
        # If B has more elements than A, it's impossible to match
        if len(brr) > len(arr):
            return "NO"

        # Get the largest value from B (negated back to positive)
        largest_b = -heappop(brr)
        
        # If the largest element in B matches the last element in A, remove it
        if largest_b == arr[-1]:
            arr.pop()
            continue
        
        # If the largest element in B is smaller than the last element in A, it's impossible
        if largest_b < arr[-1]:
            return "NO"

        # Split the largest element in B into two smaller parts
        half = largest_b // 2
        heappush(brr, -half)
        heappush(brr, -(largest_b - half))
    
    return "YES"

# Read input
t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    brr = list(map(int, input().split()))
    print(can_transform(n, m, arr, brr))
