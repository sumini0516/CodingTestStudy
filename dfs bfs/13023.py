import sys
from collections import defaultdict

def dfs(position, depth):
    global finished
    visited[position] = 1
    if depth == 4:
        finished = True
        return
    for i in relationship[position]:
        if not visited[i]:
            dfs(i, depth + 1)
            visited[i] = 0

N, M = map(int, input().split(" "))
relationship = defaultdict(list)
visited = [0] * N
finished = False

for i in range(M):
    a, b = map(int, input().split(" "))
    relationship[a].append(b)
    relationship[b].append(a)

for i in range(N):
    dfs(i, 0)
    visited[i] = 0
    if finished:
        break

if finished:
    print(1)
else:
    print(0)
