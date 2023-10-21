import heapq

def solution(prices):
    length = len(prices)
    answer = [i for i in range(length -1, -1, -1)]
    stack = [0]
    for i in range(1, length):
        while stack and prices[stack[-1]] > prices[i]:
            j = stack.pop()
            answer[i] = i - j
        stack.append(i)

    return answer


print(solution([1, 2, 3, 2, 3]))
print(solution([9, 2, 3, 2, 3]))