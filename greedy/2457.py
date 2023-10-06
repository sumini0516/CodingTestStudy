import sys

input = sys.stdin.readline

N = int(input())
flowers = list()
start_month = 3
start_day = 1
end_month = 11
end_day = 30

for i in range(N):
    SM, SD, EM, ED = map(int, input().split())
    flowers.append((SM, SD, EM, ED))

print(flowers)

