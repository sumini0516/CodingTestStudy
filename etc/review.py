import sys
from collections import defaultdict
import heapq

input = sys.stdin.readline
INF = int(1e9)

def dijkstra(start, end):
    distance = [INF] * (N + 1)
    queue = list()
    heapq.heappush(queue, (0, start))
    distance[start] = 0
    while queue:
        cost, node = heapq.heappop(queue)
        if distance[node] < cost:
            continue
        for next_cost, next_node in graph[node]:
            compare = distance[node] + next_cost
            if compare < graph[next_node]:
                distance[node] = compare
                heapq.heappush(queue, (compare, next_node))


N, M = map(int, input().split(" "))
graph = defaultdict(list)
flag = 1
for i in range(M):
    a, b, c = map(int, input().split(" "))
    graph[a].append((b, c))
    graph[b].append((a, c))
V1, V2 = map(int, input().split(" "))

