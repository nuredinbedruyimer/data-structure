n, k = list(map(int, input().split()))
arr = list(map(int, input().split()))
brr = list(map(int, input().split()))

mapp = []

for i in range(n):
    mapp.append([arr[i], brr[i], arr[i] - brr[i]])
mapp.sort(key=lambda x : x[2])
ans = 0
for i in range(k):
    ans += mapp[i][0]
for i in range(k, n):
    if mapp[i][2] <= 0:
        ans += mapp[i][0]
    else:
        ans += mapp[i][1]
        
print(ans)