import sys

input = sys.stdin.readline

N = int(input())
dp = [0] * N
drink = [0] * N

for i in range(N):
    M = int(input())
    drink[i] = M
print(drink)
dp[0] = drink[0]
if N > 1:
    dp[1] = drink[0] + drink[1]
if N > 2:
    dp[2] = max(dp[1], drink[0] + drink[2], drink[1] + drink[2])

for i in range(3, N):
    dp[i] = max(dp[i - 1], drink[i] + dp[i - 3] + drink[i - 1], drink[i] + dp[i - 2])

print(dp[-1])