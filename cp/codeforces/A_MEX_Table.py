test = int(input())
for _ in range(test):
    n, m = list(map(int, input().split()))
    print(max(n, m) + 1)