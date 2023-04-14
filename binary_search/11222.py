import sys
from collections import deque

input = sys.stdin.readline

N, C = map(int, input().split())

houses = list()

for i in range(N):
    x = int(input())
    houses.append(x)

houses.sort()
answer = 0

start = 1
end = houses[-1]

while start <= end:
    mid = (start + end) // 2
    current = houses[0]
    cnt = 1
    for i in range(len(houses)):
        if current + mid <= houses[i]:
            cnt += 1
            current = houses[i]

    if cnt >= C:
        answer = mid
        start = mid + 1
    else:
        end = mid - 1

print(answer)