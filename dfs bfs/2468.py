import sys
from collections import deque

input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(start_x, start_y, visited):
    queue = deque()
    queue.append((start_x, start_y))
    visited[start_x][start_y] = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0 and graph[nx][ny] > k:
                visited[nx][ny] = 1
                queue.append((nx, ny))

    return


N = int(input())
max_num = 0
answer = 0

graph = list()

for i in range(N):
    M = list(map(int, input().split()))
    graph.append(M)
    max_num = max(max_num, max(M))

# print(max_num)
for k in range(max_num):
    visited = [[0] * (N) for _ in range(N)]
    count = 0
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0 and graph[i][j] > k:
                bfs(i, j, visited)
                count += 1
    # print(count)
    answer = max(count, answer)

print(answer)