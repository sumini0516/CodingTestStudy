from collections import defaultdict
import sys
import heapq

input = sys.stdin.readline

n = int(input())
m = int(input())
INF = int(1e9)
distance = [INF] * (n + 1)
prev_node = [0] * (n + 1)
graph = defaultdict(list)

for i in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

start, end = map(int, input().split())

q = []
heapq.heappush(q, (0, start))
distance[start] = 0
while q:
    weight, node = heapq.heappop(q)
    if distance[node] < weight:
        continue
    for adj_node, adj_weight in graph[node]:
        cost = weight + adj_weight
        if cost < distance[adj_node]:
            prev_node[adj_node] = node
            distance[adj_node] = cost
            heapq.heappush(q, (cost, adj_node))

path = [end]
now = end

while now != start:
    now = prev_node[now]
    path.append(now)

path.reverse()

print(distance[end])
print(len(path))
print(' '.join(map(str, path)))