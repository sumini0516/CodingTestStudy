import sys

input = sys.stdin.readline

R, C = map(int, input().split(" "))
alp = list()
visited = [[0] * C for _ in range(R)]
print(visited)

for i in range(R):
    A = input().rstrip()
    AA = list()
    for i in A:
        AA.append(i)
    alp.append(AA)

visit_alp = list()

