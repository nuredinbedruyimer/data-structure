n = int(input())
arr = list(map(int, input().split()))

i = 1
while i < n and arr[i - 1] < arr[i]:
    i += 1

j = i
while j < n and arr[j - 1] > arr[j]:
    j += 1

s_l = sorted(arr)

m_l = arr[:i - 1] + arr[i - 1:j][::-1] + arr[j:]

if m_l == s_l:
    print("yes")
    print(i, j)
    
else:
    print("no")