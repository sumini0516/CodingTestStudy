import sys
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(chicken, house):
    distance_all = 0
    for hc, hr in house:
        distance = int(1e9)
        for cc, cr in chicken:
            distance = min(distance, abs(hc - cc) + abs(hr - cr))
        distance_all += distance
    global answer
    answer = min(distance_all, answer)

def close(cnt, chicken, house):
    if cnt <= M:
        bfs(chicken, house)
        return
    for x, y in chicken:
        A = chicken[-1]
        chicken.pop()
        close(cnt - 1, chicken, house)
        chicken.append(A)

N, M = map(int, input().split(" "))
graph = [list(map(int, input().split())) for _ in range(N)]
chicken, house = list(), list()

for i in range(N):
    for j in range(N):
        if graph[i][j] == 2:
            chicken.append((i, j))
        elif graph[i][j] == 1:
            house.append((i, j))

answer = int(1e9)
close(len(chicken), chicken, house)
print(answer)