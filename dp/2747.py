import sys
import collections

input = sys.stdin.readline
dp = [0] * 50

N = int(input())


def fibo(N):
    dp[0] = 0
    dp[1] = 1
    for i in range(2, N + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
        # print(dp[i])
    return dp[N]

print(fibo(N))
