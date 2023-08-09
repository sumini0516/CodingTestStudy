import sys
from collections import defaultdict

input = sys.stdin.readline
sys.setrecursionlimit(10**9)
graph = defaultdict(list)

def bfs(node, dist):
    for next_node, next_dist in graph[node]:
        if visited[next_node] == -1:
            visited[next_node] = dist + next_dist
            bfs(next_node, dist + next_dist)

    return max(visited)

N = int(input())
for i in range(N - 1):
    u, w, v = map(int, input().rstrip().split(" "))
    graph[u].append((w, v))
    graph[w].append((u, v))

visited = [-1] * (N + 1)
visited[1] = 0
answer = bfs(1, 0)
A = visited.index(answer)

visited = [-1] * ( N + 1)
visited[A] = 0
answer = bfs(A, 0)

print(answer)