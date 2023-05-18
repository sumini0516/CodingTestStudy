import sys
import math
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(i, j):
    queue = deque()
    queue.append((i, j))
    visited[i][j] = 1
    union = [(i, j)]
    count = population[i][j]
    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue
            if visited[nx][ny] == 1:
                continue
            if L <= abs(population[nx][ny] - population[x][y]) <= R:
                union.append((nx, ny))
                visited[nx][ny] = 1
                queue.append((nx, ny))
                count += population[nx][ny]
    for x, y in union:
        population[x][y] = math.floor(count/len(union))

    return len(union)

input = sys.stdin.readline
N, L, R = map(int, input().split(" "))
result = 0
population = list()

for i in range(N):
    population.append(list(map(int, input().split())))

while True:
    visited = [[0] * N for _ in range(N)]
    flag = 0
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                if bfs(i, j) > 1:
                    flag = 1
    if not flag:
        break
    result += 1

print(result)
