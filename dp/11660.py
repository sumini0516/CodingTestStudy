import sys

input = sys.stdin.readline

graph = []

N, M = map(int, input().split(" "))
dp = [[0] * (N + 1) for _ in range(N + 1)]

for i in range(N):
    A = list(map(int, input().rstrip().split(" ")))
    graph.append(A)

for i in range(1, N + 1):
    for j in range(1, N + 1):
        dp[i][j] = dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1] + graph[i - 1][j - 1]

for j in range(M):
    x1, y1, x2, y2 = map(int, input().split(" "))
    answer = dp[x2][y2] - dp[x2][y1 - 1] - dp[x1 - 1][y2] + dp[x1 - 1][y1 - 1]
    print(answer)