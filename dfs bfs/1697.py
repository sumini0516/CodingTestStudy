import sys
from collections import deque

input = sys.stdin.readline

N, K= map(int, input().split(" "))
visited = [-1] * (K + 1)
visited[N] = 0
queue = deque()
queue.append((N, 0))

while queue:
    n, time = queue.popleft()
    if n == K:
        break
    for nn in (n - 1, n + 1, n * 2):
        if 0 <= nn <= K and visited[nn] == -1:
            visited[nn] = time + 1
            queue.append((nn, time + 1))

print(visited[K])