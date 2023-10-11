import sys

# 검은색(white[i][j] == 1) 갯수 새기

input = sys.stdin.readline

answer = 0
white = [[0] * 100 for _ in range(100)]
black = list()

N = int(input())
for i in range(N):
    x, y = map(int, input().split(" "))
    black.append([x, y])

for x1, y1 in black:
    x2 = x1 + 10
    y2 = y1 + 10
    for i in range(x1, x2):
        for j in range(y1, y2):
            if white[i][j] == 0:
                white[i][j] = 1

for i in range(len(white)):
    answer += white[i].count(1)

print(answer)