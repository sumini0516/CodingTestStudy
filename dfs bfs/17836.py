import sys
from collections import deque
import copy

input = sys.stdin.readline
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(start_x, start_y, end_x, end_y, graph, visited):
    queue = deque()
    queue.append((start_x, start_y))
    graph[start_x][start_y] = 0
    visited[start_x][start_y] = 1
    if start_x == 0 and start_y == 0:
        flag = 0
    else:
        flag = 1
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if flag == 0:
                if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == 0:
                    if graph[nx][ny] == 0 or graph[nx][ny] == 2:
                        graph[nx][ny] = graph[x][y] + 1
                        queue.append((nx, ny))
                        visited[nx][ny] = 1
            else:
                if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] <= 1 and visited[nx][ny] == 0:
                    graph[nx][ny] = graph[x][y] + 1
                    queue.append((nx, ny))
                    visited[nx][ny] = 1

    if flag == 0 and graph[end_x][end_y] == 2:
        return 10000
    else:
        return graph[end_x][end_y]


N, M, T = map(int, input().split())
graph1 = [[0] for _ in range(N)]
visited1 = [[0] * (M) for _ in range(N)]
visited2 = [[0] * (M) for _ in range(N)]

for i in range(N):
    a = list(map(int, input().split(" ")))
    graph1[i] = a

for i in range(N):
    for j in range(M):
        if graph1[i][j] == 2:
            gram_x = i
            gram_y = j

graph2 = copy.deepcopy(graph1)
A = bfs(0, 0, gram_x, gram_y, graph1, visited1)
B = bfs(gram_x, gram_y, -1, -1, graph1, visited1)
result1 = A + B
result2 = bfs(0, 0, -1, -1, graph2, visited2)
print(result1)
print(result2)

result = min(result1, result2)

if result > T or result == 0:
    print("Fail")
else:
    print(result)
