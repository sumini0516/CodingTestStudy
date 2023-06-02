import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split(" "))

position = deque()
position.append((N, 0))

while position:
    now, time = position.popleft()
    if now == K:
        print(time)
        break
    else:
        if now * 2 <= K:
            position.append((now * 2, time))
        else:
            if now > K:
                position.append((now - 1, time + 1))
            else:
                position.append((now + 1, time + 1))

