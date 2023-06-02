# dp[0] = stair[0]
# dp[1] = stair[0] + stair[1]
# dp[2] = max(stair[0] + stair[2], stair[1] + stair[2])
# dp[3:] = max(dp[i - 3] + stair[i - 1] + s[i], dp[i - 2] + s[i])

import sys

input = sys.stdin.readline

N = int(input())
stair = [0] * (N + 1)
dp = [0] * (N + 1)

for i in range(N):
    M = int(input())
    stair[i] = M

dp[0] = stair[0]
dp[1] = stair[1] + stair[0]

if N >= 3:
    dp[2] = max(stair[0] + stair[2], stair[1] + stair[2])
    for i in range(3, N):
        dp[i] = max(dp[i - 3] + stair[i - 1] + stair[i], dp[i - 2] + stair[i])

print(dp[N - 1])
