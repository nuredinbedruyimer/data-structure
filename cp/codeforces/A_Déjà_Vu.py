test = int(input())

for _ in range(test):
    word = input()
    if len(word) == word.count("a"):
        print("NO")
    else:
        ans = ""
        if word == word[::-1]:
            ans = word + "a"
        else:
            half = len(word) // 2
            ans = word[:half] + "a" + word[half:]
        print("YES")
        print(ans)
        