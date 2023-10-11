import sys
from collections import deque

input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(start_x, start_y, flag):
    queue = deque()
    queue.append((start_x, start_y))

    if flag == 0:
        visited_normal[start_x][start_y] = 1
    else:
        visited_not[start_x][start_y] = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if flag == 0 and visited_normal[nx][ny] == 0: #일반인의 경우
                    if colors[nx][ny] == colors[x][y]:
                        visited_normal[nx][ny] = 1
                        queue.append((nx, ny))
                elif flag == 1 and visited_not[nx][ny] == 0: #색약의 경우
                    if colors[x][y] in ("R","G"):
                        if colors[nx][ny] in ("R","G"):
                            visited_not[nx][ny] = 1
                            queue.append((nx, ny))
                    else:
                        if colors[nx][ny] == colors[x][y]:
                            visited_not[nx][ny] = 1
                            queue.append((nx, ny))

N = int(input())
colors = list()
answer = [0, 0]
visited_normal = [[0] * N for _ in range(N)]
visited_not = [[0] * N for _ in range(N)]

for i in range(N):
    color = input().rstrip()
    li = list()
    for c in color:
        li.append(c)
    colors.append(li)

for i in range(N):
    for j in range(N):
        if visited_normal[i][j] == 0:
            dfs(i, j, 0)
            answer[0] += 1
            # print(answer)
        if visited_not[i][j] == 0:
            dfs(i, j, 1)
            answer[1] += 1
            # print(answer)

print(answer[0], answer[1], end = " ")