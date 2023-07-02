import sys
from collections import deque

input = sys.stdin.readline

def bfs(start):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]

    queue = deque()
    queue.append((start[0], start[1]))
    visited[start[0]][start[1]] = 0

    while queue:
        x, y = queue.popleft()
        print(x, y)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if graph[nx][ny] == 1 and 0 <= nx < M and 0 <= ny < N and visited[nx][ny] == -1:
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx, ny))
    return



N, M = map(int, input().split(" "))
graph = list()
visited = [[-1] * M for _ in range(N)]

for i in range(N):
    A = list(map(int, input().rstrip().split(" ")))
    graph.append(A)
    if 2 in A:
        start = (i, A.index(2))

for i in range(N):
    for j in range(M):
        if visited[i][j] == -1:
            print(0, end = " ")
        else:
            print(visited[i][j], end = " ")
    print("\n")

