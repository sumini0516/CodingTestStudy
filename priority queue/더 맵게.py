import heapq


def solution(scoville, K):
    answer = 0
    heap = []
    for scov in scoville:
        heapq.heappush(heap, scov)

    while True:
        if heap[0] >= K:
            break
        if len(heap) == 1 and heap[0] < K:
            answer = -1
            break
        num1 = heapq.heappop(heap)
        num2 = heapq.heappop(heap)
        num3 = num1 + (num2 * 2)
        heapq.heappush(heap, num3)
        answer += 1

    return answer