import queue
import sys
from collections import defaultdict


input = sys.stdin.readline
graph = defaultdict(list)

N = int(input())
for i in range(N):
    u, w, v = map(int, input().split(" "))
    graph[u].append((w, v))

