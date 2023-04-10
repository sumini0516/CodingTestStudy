import sys
import heapq

input = sys.stdin.readline

N = int(input())
M = int(input())

INF = int(1e9)

graph = [[] * (M + 1) for _ in range(M + 1)]
distance = [INF] * (M + 1)

for i in range(M):
    U, W, V = map(int, input().split())
    graph[U].append((W, V))

def dijkstra(start, end):
    queue = []
    heapq.heappush(queue, (start, 0))
    distance[start] = 0

    while (queue):
        now, dist = heapq.heappop(queue)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(queue, (i[0], cost))


start, end = map(int, input().split())
dijkstra(start, end)

print(distance[end])