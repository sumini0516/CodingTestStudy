import heapq
import sys

input = sys.stdin.readline

N = int(input())
course = list()
answer = 1

for i in range(N):
    S, T = map(int, input().split())
    course.append((S, T))

course.sort()
classroom = list()
heapq.heappush(classroom, course[0][1])

for i in range(1, N):
    compare = course[i]
    nearest_class = heapq.heappop(classroom)
    if nearest_class <= compare[0]:
        heapq.heappush(classroom, compare[1])
    else:
        heapq.heappush(classroom, nearest_class)
        heapq.heappush(classroom, compare[1])
        answer += 1

print(answer)
