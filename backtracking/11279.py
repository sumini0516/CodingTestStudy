import heapq
import sys

heap = []

N = int(input())

for i in range(N):
    x = sys.stdin.readline().rstrip()

    if x == '0':
        if len(heap) == 0:
            print(0, end="\n")
        else:
            result = heapq.heappop(heap)
            print(-1 * result, end = "\n")
    else:
        heapq.heappush(heap, -1 * int(x))