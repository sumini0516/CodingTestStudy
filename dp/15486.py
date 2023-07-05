import sys

input = sys.stdin.readline

N = int(input())
dp = [0] * (N + 1)
TP = list()

for _ in range(N):
    T, P = map(int, input().split(" "))
    TP.append((T, P))

