import heapq
import sys
import math

N= int(input())
heap = []
for _ in range(N):
    M = int(sys.stdin.readline().rstrip())
    heap2 = []
    if int(M) == 0:
        if len(heap) == 0:
            print("0", end="\n")
        else:
            ans = heapq.heappop(heap)
            print(ans[1], end = "\n")
    else:
        heapq.heappush(heap, [abs(M), int(M)])
        # print(heap)