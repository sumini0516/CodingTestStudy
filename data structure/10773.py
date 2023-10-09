import sys

input = sys.stdin.readline

K = int(input())
num = list()

for i in range(K):
    M = int(input())
    if M == 0:
        num.pop()
    else:
        num.append(M)

print(sum(num))