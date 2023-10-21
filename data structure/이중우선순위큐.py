import heapq

def solution(operations):
    answer = []
    heap = []
    max_heap = []
    for i in operations:
        i_split = i.split()
        operation = i_split[0]
        num = int(i_split[1])
        if operation == "I":
            heapq.heappush(heap, num)
            heapq.heappush(max_heap, ((-1)*num, num))
        else:
            if len(heap) == 0:
                continue
            elif num == -1: #최솟값을 지워준다
                min_value = heapq.heappop(heap)
                max_heap.remove((-1 * min_value, min_value))
            elif num == 1: #최댓값을 지워준다
                max_value = heapq.heappop(max_heap)
                heap.remove(max_value[1])
    if len(heap) == 0:
        answer.append(0)
        answer.append(0)
    else:
        answer.append(max_heap[0][1])
        answer.append(heap[0])
    return answer