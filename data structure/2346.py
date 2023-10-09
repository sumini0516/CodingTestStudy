from collections import deque
import sys

input = sys.stdin.readline

N = int(input())
ballons = deque(enumerate(map(int, input().split(" "))))
answer = list()

# print(N)
# print(ballons)

while ballons:
    idx, paper = ballons.popleft()
    answer.append(idx + 1)
    #deque.rotate(-1): 원형 큐를 반시계 방향으로 1칸 회전
    #deque.rotate(1): 원형 큐를 시계방향으로 1칸 회전
    if paper > 0:
        ballons.rotate(-(paper - 1))
    elif paper < 0:
        ballons.rotate(-paper)

print(' '.join(map(str, answer)))