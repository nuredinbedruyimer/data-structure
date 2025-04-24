s = input()
maxi = 0
mini = 0
arr = []
count = 0
for c in s:
    if (count % 2 == 0) and c == "1":
        count += 1
    else:
        count -= 1
    mini = min(mini, count)
    maxi = max(maxi, count)
    arr.append((mini, maxi))
print(arr)
    