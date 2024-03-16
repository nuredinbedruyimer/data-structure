test = int(input())

power = [ 4 **i for i in range(64)]

for _ in range(test):
     n = int(input())
     
     ans = -1
     count = 0
     
     for p in power:
         
         
         if n // p <= 3:
             ans = n // p
             break
         count +=1
     print(2**count)
     