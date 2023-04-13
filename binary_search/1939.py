import sys
from collections import deque

input = sys.stdin.readline


def bfs(weight):
    queue = deque()
    queue.append(A)
    visited = [0] * (N + 1)
    visited[A] = 1

    while (queue):
        V = queue.popleft()

        for i, w in graph[V][1:]:
            if visited[i] == 0 and w >= weight:
                visited[i] = 1
                queue.append(i)

    if visited[B]:
        return True
    else:
        return False


N, M = map(int, input().split())

graph = [[0] for _ in range(N + 1)]
# print(graph)

for i in range(M):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])

# print(graph)

A, B = map(int, input().split())

start = 0
end = 1000000000

while (start <= end):
    mid = (start + end) // 2

    if bfs(mid):
        result = mid
        start = mid + 1

    else:
        end = mid - 1

print(result)