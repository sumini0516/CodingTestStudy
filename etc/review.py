import sys
from collections import deque
import copy

input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    queue = deque()
    tmp_graph = copy.deepcopy(graph)
    for i in range(N):
        for j in range(M):
            if tmp_graph[i][j] == 2:
                queue.append((i, j))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0 <= nx < N and 0 <= ny < M:
                if tmp_graph[nx][ny] == 0:
                    tmp_graph[nx][ny] = 2
                    queue.append((nx, ny))

    global answer
    ans = 0
    for i in range(N):
        ans += graph[i].count(0)
    answer = max(answer, ans)

def makewall(cnt):
    if cnt == 3:
        bfs()
        return
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 2:
                graph[i][j] = 1
                makewall(cnt + 1)
                graph[i][j] = 2

N, M = map(int, input().split())
graph = []
for i in range(N):
    graph.append(list(map(int, input().split())))
answer = 0
makewall(0)
print(answer)