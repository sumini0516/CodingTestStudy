import sys
from collections import defaultdict

input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
sum = 0

N = int(input())

seat = [[0] * (N + 1) for _ in range(N + 1)]

student = defaultdict(list)

for _ in range(N ** 2):
    info = list(map(int, input().split()))
    student_num = info[0]
    student_like = info[1:]
    student[student_num] = student_like

    #앉을 수 있는 자리 후보군
    able = []

    for x in range(1, N + 1):
        for y in range(1, N + 1):
            if seat[x][y] == 0:
                like = 0
                empty = 0
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if 1 <= nx < N + 1 and 1 <= ny < N + 1:
                        if seat[nx][ny] == 0:
                            empty += 1
                        if seat[nx][ny] in student[student_num]:
                            like += 1
                able.append((like, empty, x, y))
    able = sorted(able, key = lambda x : (-x[0], -x[1], x[2], x[3]))
    seat[able[0][2]][able[0][3]] = student_num

for i in range(1, N + 1):
    for j in range(1, N + 1):
        count = 0
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]
            if 1 <= nx < N + 1 and 1 <= ny < N + 1:
                if seat[nx][ny] in student[seat[i][j]]:
                    count += 1

        if count != 0:
            sum += 10 ** (count - 1)

print(sum)
