import sys

input = sys.stdin.readline

N = int(input())
stairs = list()
dp = [0] * N

for i in range(N):
    stairs.append(int(input()))

dp[0] = stairs[0]

if N > 1:
    dp[1] = stairs[0] + stairs[1]

if N > 2:
    dp[2] = max(stairs[0] + stairs[2], stairs[1] + stairs[2])

for i in range(3, N):
    dp[i] = max(stairs[i] + dp[i - 2], dp[i - 3] + stairs[i] + stairs[i - 1])

print(dp[-1])