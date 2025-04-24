test = int(input())

def helper(sequence, char):
    count = 0
    for curr_char in sequence:
        if curr_char != char:
            count += 1

    return count

for _ in range(test):
    n = int(input())
    
    word = list(input())
    
    largest_sequence = []
    for i in range(n):
        while largest_sequence and word[largest_sequence[-1]] < word[i]:
            largest_sequence.pop()
        
        largest_sequence.append(i)
        
    
    x = []
    char = word[largest_sequence[0]]
    
    
    for index in largest_sequence:
        x.append(word[index])
        word[index] = "-1"
    opt = helper(x, char) 
    x.sort()
    i = 0
    for index in range(n):
        if word[index] == "-1":
            word[index] = x[i]
            i += 1
    if word == sorted(word):
        print(opt)
    else:
        print(-1)
    
        
        
    
        
    
    