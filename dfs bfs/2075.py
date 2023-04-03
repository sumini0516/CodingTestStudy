import heapq
import sys

N = int(input())
heap = []
# print(heap)

for _ in range(N):
    num = list(map(int, input().split()))
    if len(heap) == 0:
        for n in num:
            heapq.heappush(heap, n)
            # print(heap)
    else:
        # print(n)
        for n in num:
            if heap[0] < n:
                heapq.heappop(heap)
                heapq.heappush(heap, n)
                # print(heap)

print(heap[0])
