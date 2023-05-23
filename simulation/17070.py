# 가로 파이프 > 가로, 대각선
# 세로 파이프 > 세로, 대각선
# 대각선 파이프 > 대각선, 가로, 세로
# board : 3차원 짐 그래프
# 아이디어:
# (1) 첫 번째 행에는 항상 가로 파이프만 올 수 있따.
# (2) 1열에는 파이프의 끝이 올 수 없다. (항상 시작 파이프가 가로이기 때문)
# (3) 가로 파이프 : 왼쪽 칸의 가로 파이프 개수 + 왼쪽 칸의 대각선 파이프 개수
# (4) 세로 파이프 : 위쪽 칸의 세로 파이프 개수 + 위쪽 칸의 대각선 파이프 개수
# (5) 대각선 파이프 : 왼쪽 위 대각선 칸의 (가로 파이프 개수 + 세로 파이프 개수 + 대각선 파이프 개수)
# dp[0][row][col] > 가로 파이프에 대한 dp
# dp[1][row][col] > 대각선 파이프에 대한 dp
# dp[2][row][col] > 세로 파이프에 대한 dp

import sys

input = sys.stdin.readline


def pipe():
    dp[0][0][1] = 1
    # 첫 번째 행을 채우는 과정
    for i in range(2, N):
        if board[0][i] == 0:
            dp[0][0][i] = dp[0][0][i - 1]

    for r in range(1, N):
        for c in range(1, N):
            # 대각선 파이프 추가 과정
            if board[r][c] == 0 and board[r][c - 1] == 0 and board[r - 1][c] == 0:
                dp[1][r][c] = dp[0][r - 1][c - 1] + dp[1][r - 1][c - 1] + dp[2][r - 1][c - 1]
            # 가로, 세로 파이프 추가 과정
            if board[r][c] == 0:
                dp[0][r][c] = dp[0][r][c - 1] + dp[1][r][c - 1]
                dp[2][r][c] = dp[2][r - 1][c] + dp[1][r - 1][c]
    result = sum(dp[i][N - 1][N - 1] for i in range(3))
    # print(dp)
    return result


N = int(input())
board = list()
dp = [[[0 for _ in range(N)] for _ in range(N)] for _ in range(3)]

for i in range(N):
    M = list(map(int, input().split(" ")))
    board.append(M)

print(pipe())
