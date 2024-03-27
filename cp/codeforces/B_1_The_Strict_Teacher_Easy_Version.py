test = int(input())


for _ in range(test):
    n, m, q = list(map(int, input().split()))
    mrr = list(map(int, input().split()))
    qrr = list(map(int, input().split()))
    
    
    if mrr[0] <= qrr[0] <= mrr[1]:
        diff = max(qrr[0] - mrr[0], mrr[1] - qrr[0]) - min(qrr[0] - mrr[0], mrr[1] - qrr[0]) 
        ans = min(qrr[0] - mrr[0], mrr[1] - qrr[0])  + diff // 2
        print(ans)
    elif mrr[0] > qrr[0]:
        print(mrr[0] - qrr[0])
    else:
        print(qrr[0] - mrr[1])