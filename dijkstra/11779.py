import heapq
import sys
import heapq
from collections import defaultdict

input = sys.stdin.readline

def dijkstra(start):
    q =[]
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        #노드 가는데 드는 비용, 방문할 노드
        weight, node = heapq.heappop(q)
        #다음 방문할 노드까지의 거리가 더 길면 패스
        if distance[node] < weight:
            continue
        #아니면

            #다음 방문할 노드와 이어진 노드들을 다 비교하는데
        for adj_node, adj_weight in graph[node]:
            # 방문할 노드 + 이어진 노드 비용
            cost = weight + adj_weight
            if cost < distance[adj_node]:
                prev_node[adj_node] = node
                distance[adj_node] = cost
                heapq.heappush(q, (cost, adj_node))

    return distance, prev_node

N = int(input())
M = int(input())
INF = int(1e9)

graph = defaultdict(list)
distance = [INF] * (N + 1)
prev_node = [0] * (N + 1)

for i in range(M):
    u, w, v = map(int, input().split())
    graph[u].append((w, v))

# print(graph)
start, end = map(int, input().split())

d, p = dijkstra(start)

path = [end]
now = end
while now != start:
    now = prev_node[now]
    path.append(now)

path.reverse()

print(d[end])
print(len(path))
print(' '.join(map(str, path)))