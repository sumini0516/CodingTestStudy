import sys

input = sys.stdin.readline

N = int(input())
num = list(map(int, input().rstrip().split(" ")))
dp = [0] * N
dp[0] = num[0]

for i in range(1, N):
    dp[i] = max(num[i], dp[i - 1] + num[i])

print(max(dp))