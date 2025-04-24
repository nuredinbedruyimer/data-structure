n, k = list(map(int, input().split()))
word = input()
chars_bank = input()

"""
a =  0 
b = 1
c = 2
.
,
z = 25
a = 97 - 97
b = 98 - 97
c = 99

a 
a a
a a
2

a a b
   l 
 b a

1 + 2  +  2

"""
alpha_map = [i for i in range(26)]



for char in chars_bank:
    char_index = ord(char) - ord("a")
    alpha_map[char_index] += 1

#
ans = 0
left = 0

for right in range(n):
    # shirink condition
    index = ord(word[right]) - ord("a")
   
    
    
    while left <= right and right < n and alpha_map[index] == 0:
        left_index = ord(word[left]) - ord("a")
        alpha_map[left_index] += 1
        

        
        
        left += 1
    alpha_map[index] -= 1
    
    
    ans += right - left + 1
print(ans)