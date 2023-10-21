import sys

input = sys.stdin.readline

N = int(input())
dp = [0] * (N + 1)
T = [0] * (N + 1)
P = [0] * (N + 1)

for i in range(N):
    t, p = map(int, input().split(" "))
    T[i + 1] = t
    P[i + 1] = p

for i in range(1, N + 1):
    dp[i] = max(dp[i], dp[i - 1])
    complete = i + T[i] - 1
    if complete <= N:
        dp[complete] = max(dp[complete], dp[i - 1] + P[i])
    # print(dp)

print(max(dp))