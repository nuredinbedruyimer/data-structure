def main():
    n = int(input())
    mod = 10**9 + 7

    dp = [0] * (n + 1)
    dices = 6
    dp[0] = 1  

    for i in range(1, n + 1):
        for dice in range(1, dices + 1):
            if dice > i:
                continue
            dp[i] = (dp[i] + dp[i - dice]) % mod

    print(dp[n])

if __name__ == "__main__":
    main()
