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

for i in graph:
    print(i, end="\n")

def dijkstra(start, end):
    queue = []
    heapq.heappush(queue, (start, 0))
    distance[start] = 0
    route = []
    route.append(start)

    while (queue):
        now, dist = heapq.heappop(queue)
        print(now, dist)
        save_route = ""
        flag = 0
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                # print(i[1], cost)
                distance[i[0]] = cost
                heapq.heappush(queue, (i[0], cost))
                print(queue)
                print(distance)
                save_route = i[0]
                flag = 1
        if flag == 1:
            route.append(save_route)

    return distance[end], route


start, end = map(int, input().split())
ans, route = dijkstra(start, end)
print(ans)
print(len(route))
print(route)