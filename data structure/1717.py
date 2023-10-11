import sys
sys.setrecursionlimit(1000000)

input = sys.stdin.readline

N, M = map(int, input().rstrip().split(" "))
parent = [i for i in range(N + 1)]

def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

for _ in range(M):
    opr, A, B = map(int, input().rstrip().split())
    if opr == 0:
        union_parent(A, B)
    else:
        if find_parent(A) == find_parent(B):
            print("YES")
        else:
            print("NO")