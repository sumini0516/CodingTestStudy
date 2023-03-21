from collections import deque

def bfs(V):
    count = 0
    queue = deque()
    queue.append(V)
    visited[V] = 1
    while (queue):
        V = queue.popleft()
        # print(V)
        for i in range(N + 1):
            if visited[i] == 0 and matrix[V][i] == 1:
                queue.append(i)
                visited[i] = 1
                count += 1
    # print(visited)
    return count


N = int(input())
M = int(input())
matrix = matrix = [[0] * (N + 1) for i in range(N + 1)]
visited = [0] * (N + 1)
for i in range(M):
    a, b = map(int, input().split())
    matrix[a][b] = matrix[b][a] = 1
# print(matrix)
print(bfs(1))
