import sys

input = sys.stdin.readline

N = int(input())
M = int(input())

INF = int(1e9)

graph = [[INF] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
    u, w, v = map(int, input().split())
    graph[u][w] = min(v, graph[u][w])

#플로이드-워셜 알고리즘
for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if i == j:
                graph[i][j] = 0
            else: #경로를 거치는 것 or 직접 가는 것 or 이전 경로들
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for i in graph[1:]:
    for j in i[1:]:
        if j == INF:
            print(0, end = " ")
        else:
            print(j, end = " ")
    print()