import sys

input = sys.stdin.readline

N = int(input())
wines = list()
dp = [0] * N

for i in range(N):
    wine = int(input())
    wines.append(wine)

dp[0] = wines[0]

if N > 1:
    dp[1] = wines[0] + wines[1]

if N > 2:
    dp[2] = max(wines[2] + wines[1], wines[2] + wines[0], dp[1])

for i in range(3, N):
    #(1) 현재 와인 잔을 마시지 않고 패스한다 > dp[i - 1]
    #(2) 두번째 전 최댓값과 현재 와인 잔을 마신다 > dp[i - 2] + wines[i]
    #(3) 세번째 전 최댓값과 바로 전 와인과 현재 와인 잔을 마신다 > dp[i - 3] + wines[i - 1] + wines[i]
    dp[i] = max(dp[i - 1], dp[i - 2] + wines[i], dp[i - 3] + wines[i - 1] + wines[i])

print(dp[-1])