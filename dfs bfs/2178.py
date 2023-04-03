from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(start_x, start_y):
    queue = deque()
    queue.append((start_x, start_y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 1:
                queue.append((nx, ny))
                graph[nx][ny] = graph[x][y] + 1
    # print(graph)
    return graph[N - 1][M - 1]

N, M = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().rstrip())))

print(bfs(0, 0))
