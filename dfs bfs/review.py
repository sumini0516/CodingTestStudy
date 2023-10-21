import sys
from collections import deque

input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(a, b, flag, visited):
    queue = deque()
    queue.append((a, b))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0:
                if flag == 0:
                    if graph[nx][ny] == graph[x][y]:
                        queue.append((nx, ny))
                        visited[nx][ny] = 1
                else:
                    if graph[x][y] in ("R", "G"):
                        if graph[nx][ny] in ("R", "G"):
                            queue.append((nx, ny))
                            visited[nx][ny] = 1
                    else:
                        if graph[nx][ny] == graph[x][y]:
                            queue.append((nx, ny))
                            visited[nx][ny] = 1


N = int(input())
graph = [[0] * N for _ in range(N)]

for i in range(N):
    see = input()
    for j in range(N):
        graph[i][j] = see[j]

visited_normal = [[0] * N for _ in range(N)]
visited_not = [[0] * N for _ in range(N)]

answer = [0, 0]
for i in range(N):
    for j in range(N):
        if visited_normal[i][j] == 0:
            dfs(i, j, 0, visited_normal)
            answer[0] += 1
        if visited_not[i][j] == 0:
            dfs(i, j, 1, visited_not)
            answer[1] += 1

print(answer[0], answer[1])