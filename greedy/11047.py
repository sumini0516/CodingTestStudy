import sys

input = sys.stdin.readline

answer = 0
N, K = map(int, input().split(" "))
coins = list()

for i in range(N):
    M = int(input())
    if M <= K:
        coins.append(M)

coins.sort(reverse = True)

for i in coins:
    remain = K - (K // i) * i
    answer += (K // i)
    K = remain

print(answer)