import sys

input = sys.stdin.readline

N = int(input())
M = list(map(int, input().split(" ")))

dp = [1] * N

for i in range(N + 1):
    for j in range(i, N):
        if M[i] < M[j]:
            dp[j] = max(dp[j], dp[i] + 1)

print(max(dp))