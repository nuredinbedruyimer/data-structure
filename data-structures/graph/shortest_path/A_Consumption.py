n = int(input())

arr = list(map(int, input().split()))
brr = list(map(int, input().split()))


arr.sort()
brr.sort()


capacity1 = brr[-1] +  brr[-2]

total = 0
index = 0
ans = 0

if sum(arr) <= capacity1:
    print("YES")
else:
    print("NO")

