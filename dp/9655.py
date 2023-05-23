import sys

input = sys.stdin.readline

N = int(input())
dp = [0] * 1001

dp[1] = dp[3] = "SK"
dp[2] = "CY"


# 1:상근 2:창영 3:상근 4:창영 5:상근 6:창영

for i in range(4, 1001):
    if dp[i - 1] == "SK":
        dp[i] = "CY"
    else:
        dp[i] = "SK"

print(dp[N])
