from collections import defaultdict
import sys
import heapq

input = sys.stdin.readline


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


N = int(input())
M = int(input())
INF = int(1e9)

graph = defaultdict(list)
distance = [INF] * (N + 1)
for i in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

start, end = map(int, input().split())
result = dijkstra(start)

print(result[end])