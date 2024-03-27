test = int(input())

for _ in range(test):
    n = int(input())
    
    word = input()
    
    if word[0] != word[-1]:
        print("Yes")
    else:
        print("No")