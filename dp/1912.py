import sys

input = sys.stdin.readline

N = int(input())
num = list(map(int, input().split(" ")))
M = len(num)
dp = [-1000] * (M)

dp[0] = num[0]

for i in range(1, M):
    dp[i] = max(dp[i - 1] + num[i], num[i])

print(max(dp))