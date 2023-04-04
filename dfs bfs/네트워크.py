from collections import deque


def solution(N, computers):
    answer = 0
    matrix = computers
    visited = [0] * (N + 1)

    for V in range(N):
        if visited[V] == 1:
            continue
        else:
            queue = deque()
            queue.append(V)
            visited[V] = 1
            while (queue):
                V = queue.popleft()
                for i in range(N):
                    if visited[i] == 0 and matrix[V][i] == 1:
                        visited[i] = 1
                        queue.append(i)
            answer += 1

    return answer