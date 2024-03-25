import math


n = int(input())

pairs = []
for _ in range(n):
    a, b = list(map(int, input().split()))
    pairs.append([a, b])
pairs = [[0, 0]] +  pairs + [[0, 0]]

ans = 0

for i in range(1, len(pairs)):
    x = (pairs[i][0] - pairs[i- 1][0]) ** 2
    y = (pairs[i][1] - pairs[i- 1][1]) ** 2
    ans += math.sqrt(x + y)
print(ans)
    