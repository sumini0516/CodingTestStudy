import sys
from collections import defaultdict
import heapq

input = sys.stdin.readline
INF = int(1e9)

def dijkstra(start, end):
    distance = [INF] * (N + 1)
    queue = []
    heapq.heappush(queue, (0, start))
    distance[start] = 0
    while queue:
        dist, current = heapq.heappop(queue)
        if distance[current] < dist:
            continue
        for i in graph[current]:
            next_dist = i[1] + dist
            if next_dist < distance[i[0]]:
                distance[i[0]] = next_dist
                heapq.heappush(queue, (next_dist, i[0]))
    if distance[end] == INF:
        flag = 0
    # print(distance)
    return distance[end]

def check(flag, path):
    if flag == 0:
        flag = 1
        return INF
    return path

N, M = map(int, input().split(" "))
graph = defaultdict(list)
flag = 1
for i in range(M):
    a, b, c = map(int, input().split(" "))
    graph[a].append((b, c))
    graph[b].append((a, c))
V1, V2 = map(int, input().split(" "))

path1 = dijkstra(1, V1) + dijkstra(V1, V2) + dijkstra(V2, N)

path2 = dijkstra(1, V2) + dijkstra(V1, V2) + dijkstra(V1, N)

if path1 >= INF and path2 >= INF:
    print(-1)
else:
    print(min(path1, path2))