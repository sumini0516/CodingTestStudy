from collections import deque
import sys

input = sys.stdin.readline

N = int(input())
balloons = deque(enumerate(map(int, input().split(" "))))
answer = list()

while balloons:
    idx, paper = balloons.popleft()
    answer.append(idx + 1)
    if paper > 0:
        balloons.rotate(-(paper - 1))
    else:
        balloons.rotate(-paper)