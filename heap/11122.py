import math
import heapq

def solution(jobs):
    answer = 0
    time = 0
    heap = []
    for job in jobs:
        heapq.heappush(heap, job)

    disk = heapq.heappop(heap)
    time = disk[0] + disk[1]
    answer = disk[1] #대기시간

    for i in range(len(jobs) - 1):
        heap2 =[]
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

print(solution([[0, 3], [1, 9], [2, 6]]))