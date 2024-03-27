k, n = list(map(int, input().split()))




mrr = []

for i in range(n):
    arr = list(map(int, input().split()))
    mrr.append([arr[0], arr[1]])

mrr.sort()



is_loss = False
for i in range(len(mrr)):
    if mrr[i][0] >= k:
        is_loss = True
    else:
        k += mrr[i][1]
if is_loss:
    print("NO")
else:
    print("YES")
    