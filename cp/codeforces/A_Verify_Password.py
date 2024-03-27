test = int(input())

def is_digit(char):
    return char in "0123456789"


for _ in range(test):
    n = int(input())
    word = input()
    numbers = []
    characters = []
    for char in word:
        if is_digit(char):
            numbers.append(char)
        else:
            characters.append(char)
            
    ans = "NO"
    if numbers and word[0] in characters:
        ans = "NO"
    elif sorted(numbers) == numbers and sorted(characters) == characters:
        ans = "YES"
    print(ans)