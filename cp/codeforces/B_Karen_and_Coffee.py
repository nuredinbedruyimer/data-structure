from bisect import bisect_left


recipes, allowed, queries = list(map(int, input().split()))
MAX_TEMP = 200000 + 5

prefix_sum = [0 for _ in range(MAX_TEMP)]

for _ in range(recipes):
    min_temp, max_temp = list(map(int, input().split()))
    

    prefix_sum[min_temp] += 1
    
    
arr = [prefix_sum[0]]
for index in range(1, MAX_TEMP):
    arr.append(arr[-1] + prefix_sum[index])
for _ in range(queries):
    min_temp, max_temp = list(map(int, input().split()))
    diff= max_temp - min_temp + 1
    index = bisect_left(prefix_sum[min_temp: max_temp + 1], allowed)
    
    print(diff - index + 1)
    


    

    