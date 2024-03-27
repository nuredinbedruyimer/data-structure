
test = int(input())
for _  in range(test):
    vowels = ["a", "e", "i", "u", "o"]
    n = int(input())
    chars = []
    for index in range(n):
        chars.append(vowels[index % 5])
    chars.sort()
    print("".join(chars))

