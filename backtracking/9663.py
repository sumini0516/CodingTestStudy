# N-Queen
# 크기가 N*N인 체스판 위에 퀸 N개를 서로 공격할 수 없게 놓는 문제이다.
# 생각을 해보자.....
# 한 행에는 하나의 퀸 밖에 위치할 수 없다.
# 맨 위에 있는 행부터 퀸을 배치하고, 다음 행에 해당 퀸이 이동할 수 없는 위치를 찾아 퀴능ㄹ 배치
# 만약 앞선 행에 배치한 퀸으로 인해, 다음 행에 해당 퀸들이 이동할 수 없는 위치가 없을 경우, 더 이상 퀸을 배치하지 않고, 이전 퀸의 배치를 바꿈
# 맨 위의 행부터 전체 행까지 퀸의 배치가 가능한 경우의 수를 트리 형태로 만들고.. 각 경우를 맨 위의 행부터 DFS 방식으로 접근, 못하면 다른 경우를 체크
import sys

n = int(input())
ans = 0
row = [0] * n

def is_promising(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x] - row[i]) == abs(x - i):
            return False
    return True


def n_queens(x):
    global ans
    if x == n:
        ans += 1
        return
    else:
        for i in range(n):  # [x, i]에 퀸을 놓는 경우
            row[x] = i
            if is_promising(x):
                n_queens(x + 1)

n_queens(0)
print(ans)
