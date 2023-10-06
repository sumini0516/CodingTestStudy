import heapq
from collections import defaultdict
import sys

def dijkstra(start):
    queue = []
    heapq.heappush(queue, (0, start))
    distance[start] = 0
    while queue:
        cost, node = heapq.heappop(queue)
        if distance[node] < cost:
            continue
        for next_cost, next_node in graph[node]:
            weight = next_cost + cost
            if weight < graph[next_cost]:
                distance[next_cost] = weight
                heapq.heappush(queue, (weight, next_node))
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