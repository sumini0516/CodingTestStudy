import sys
from collections import defaultdict
import heapq

input = sys.stdin.readline
INF = int(1e9)

def dijkstra(start, end):
    distance = [INF] * (N + 1)
    queue = list()
    distance[start] = 0
    heapq.heappush(queue, (start, 0))
    while queue:
        node, cost = heapq.heappop(queue)
        if distance[node] < cost:
            continue
        for next_node, next_cost in graph[node]:
            if cost + next_cost < distance[next_node]:
                distance[next_node] = cost + next_cost
                heapq.heappush(queue, (next_node, cost + next_cost))
    # print(distance)
    return distance[end]

N, E = map(int, input().split(" "))
graph = defaultdict(list)

for i in range(E):
    a, b, c = map(int, input().split(" "))
    graph[a].append((b, c))
    graph[b].append((a, c))

V1, V2 = map(int, input().split(" "))

path1 = dijkstra(1, V1) + dijkstra(V1, V2) + dijkstra(V2, N)
path2 = dijkstra(1, V2) + dijkstra(V1, V2) + dijkstra(V1, N)

# print(path1)
# print(path2)

if path1 >= INF and path2 >= INF:
    print("-1")
else:
    print(min(path1, path2))