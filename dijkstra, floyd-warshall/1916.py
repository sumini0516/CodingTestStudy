import heapq
from collections import defaultdict
import sys

def dijkstra(start):
    queue = []
    heapq.heappush(queue, (0, start))
    distance[start] = 0

    while queue:
        weight, node = heapq.heappop(queue)

        if distance[node] < weight:
            continue

        for adj_node, adj_weight in graph[node]:
            cost = weight + adj_weight
            if cost < distance[adj_node]:
                distance[adj_node] = cost
                heapq.heappush(queue, (cost, adj_node))
    return distance

input = sys.stdin.readline

N = int(input())
M = int(input())
INF = int(1e9)

graph = defaultdict(list)
distance = [INF] * (N + 1)

for i in range(M):
    u, w, v = map(int, input().split())
    graph[u].append((w, v))

start, end = map(int, input().split())
result = dijkstra(start)
print(result[end])