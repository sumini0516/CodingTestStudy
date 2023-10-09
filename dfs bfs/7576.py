import sys
from collections import deque

input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def bfs():
    while queue:
        x, y = queue.popleft()
        # print(x, y)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                queue.append([nx, ny])
    return queue

M, N = map(int, input().split(" "))
graph = [list(map(int, input().split(" "))) for _ in range(N)]
queue = deque()
count_1 = 0
count_0 = 0
answer = 0

# print(graph)
for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            queue.append([i, j])
            # print([i, j])
            count_1 += 1
        elif graph[i][j] == 0:
            count_0 += 0

if count_1 == N * M:
    answer = 0
elif count_0 == N * M:
    answer = -1
else:
    bfs()
    for i in range(N):
        if 0 in graph[i]:
            answer = -1
            break
        else:
            answer = max(answer, max(graph[i]) - 1)

print(answer)