pages = int(input())

arr = list(map(int, input().split()))

index = 0
total_read = 0
ans = -1

while True:
    total_read += arr[index % 7]
    
    if total_read >= pages:
        ans = index + 1
        break
    index += 1
print(7 if ans % 7 == 0 else ans % 7)

    