from collections import defaultdict


def fun(mp, i, v, sum1, sum2):
    """
    Recursive function to calculate the minimum cost of assigning numbers to each element.

    Args:
        mp: Dictionary mapping indices to the type of number (1, 2, or 3).
        i: Current index.
        v: List of numbers.
        sum1: Sum of numbers assigned to the first set.
        sum2: Sum of numbers assigned to the second set.

    Returns:
        Minimum cost of assigning numbers.
    """

    if sum1 > sum or sum2 > sum:
        return 10**9 + 7  # Large value to represent infinity

    if i == len(v):
        if sum1 == sum2 and total_sum - sum1 - sum2 == sum1:
            return 0
        return 10**9 + 7

    if dp[i][sum1][sum2] != -1:
        return dp[i][sum1][sum2]

    ans = 10**9 + 7
    if mp[i] == 1:
        ans = min(ans, 1 + fun(mp, i + 1, v, sum1 + v[i], sum2))
    if mp[i] == 2:
        ans = min(ans, 1 + fun(mp, i + 1, v, sum1, sum2 + v[i]))
    if mp[i] == 3:
        ans = min(ans, 1 + fun(mp, i + 1, v, sum1, sum2))

    return dp[i][sum1][sum2]

def solve():
    """
    Solves the problem by calling the recursive function.
    """

    n = int(input())
    mp = defaultdict(int)
    v = []
    mp = []
    global total_sum
    total_sum = 0
    for _ in range(n):
        i, x = list(map(int, input().split()))
        mp.append(i)
        v.append(x)
        total_sum += x

    v.sort()
    global sum
    sum = total_sum // 3

    global dp
    dp = [[[-1] * (sum + 1) for _ in range(sum + 1)] for _ in range(n + 1)]

    print(fun(mp, 0, v, 0, 0))

if __name__ == "__main__":
    solve()