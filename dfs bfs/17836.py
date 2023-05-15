import sys
from collections import deque

input = sys.stdin.readline
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(start_x, start_y):
    queue = deque()
    queue.append((start_x, start_y))
    graph[start_x][start_y] = 0
    flag = 0
    save_x = -1
    save_y = -1
    while queue:
        x, y = queue.popleft()
        if x == save_x and y == save_y:
            flag = 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if flag == 0:
                if 0 <= nx < M and 0 <= ny < N:
                    if graph[nx][ny] == 0:
                        graph[nx][ny] = graph[x][y] + 1
                        queue.append((nx, ny))
                    elif graph[nx][ny] == 2:
                        save_x = nx
                        save_y = ny
                        graph[nx][ny] = graph[x][y] + 1
                        queue.append((nx, ny))
                    else:
                        continue
            else:
                if 0 <= nx < M and 0 <= ny < N:
                    if graph[nx][ny] == 0 or graph[nx][ny] == 1:
                        graph[nx][ny] = graph[x][y] + 1
                        queue.append((nx, ny))

    return graph[-1][-1]


N, M, T = map(int, input().split())
graph = [[0] for _ in range(N)]

for i in range(N):
    a = list(map(int, input().split(" ")))
    graph[i] = a

result = bfs(0, 0)
if result >= T or result == 0:
    print("Fail")
else:
    print(result)