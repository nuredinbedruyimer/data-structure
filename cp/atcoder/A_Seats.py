n = int(input())

word = input()
length = n - 1

ans = 0

for i in range(1, length):
    if word[i - 1] == word[ i  + 1] == "#" and word[i] == ".":
        ans = ans + 1
print(ans)