from collections import deque


def bfs(V):
    dist = 1
    queue = deque()
    queue.append(V)
    visited[V] = [1, 0]
    while queue:
        V = queue.popleft()
        for i in range(N + 1):
            if visited[i][0] == 0 and matrix[V][i] == 1:
                queue.append(i)
                visited[i] = [1, visited[V][1] + 1]
    return visited


N = int(input())
M = int(input())
matrix = [[0] * (N + 1) for i in range(N + 1)]
visited = [[0, 0]] * (N + 1)

for i in range(M):
    a, b = map(int, input().split())
    matrix[a][b] = matrix[b][a] = 1

result = bfs(1)
# print(result)
ans = 0
for i in result[2:]:
    if 1 <= i[1] <= 2:
        ans += 1

print(ans)