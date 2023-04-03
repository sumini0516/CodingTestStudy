from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(start_x, start_y):
    num = 1
    queue = deque()
    queue.append((start_x, start_y))
    visited[start_x][start_y] = 1

    while (queue):
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0 and matrix[nx][ny] == 1:
                visited[nx][ny] = 1
                queue.append((nx, ny))
                num += 1
    return num


N = int(input())
matrix = []
result = []
count = 0
visited = [[0] * (N + 1) for i in range(N + 1)]
for _ in range(N):
    matrix.append(list(map(int, input().rstrip())))

for i in range(N):
    for j in range(N):
        if visited[i][j] == 0 and matrix[i][j] == 1:
            count += 1
            result.append(bfs(i, j))

result.sort()
print(count)
for i in result:
    print(i)
