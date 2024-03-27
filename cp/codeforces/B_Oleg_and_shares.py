n, k = list(map(int, input().split()))
arr = list(map(int, input().split()))

is_impossible = False


    


ans = 0

min_value = min(arr)

for i in range(n):
    if (arr[i] - min_value) % k != 0:
        is_impossible = True
    else:
        ans += (arr[i] - min_value) // k 

if is_impossible:
    print(-1)
else:
    print(ans)



