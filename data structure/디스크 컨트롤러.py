import heapq
import math


def solution(jobs):
    answer = 0
    time = 0
    heap = []
    for i in jobs:
        heapq.heappush(heap, i)

    disk = heapq.heappop(heap)
    time = disk[0] + disk[1]
    answer = disk[1]

    for i in range(len(jobs) - 1):
        heap2 = []
        for i in heap:
            if i[0] <= time:
                heapq.heappush(heap2, [i[1], i[0]])

        if len(heap2) == 0:
            disk = heapq.heappop(heap)
            time = disk[0] + disk[1]
            answer += disk[1]

        else:
            disk = heapq.heappop(heap2)
            disk = [disk[1], disk[0]]
            heap.remove(disk)
            time += disk[1]
            answer += time - disk[0]

    answer = math.trunc(answer / len(jobs))

    return answer