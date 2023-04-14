import sys

input = sys.stdin.readline

N = int(input().rstrip())
region = list(map(int, input().split()))
M = int(input().rstrip())

start = 1
end = max(region)
region.sort()

while (start <= end):
    mid = (start + end) // 2
    budget = 0

    for money in region:
        if money > mid:
            budget += mid
        else:
            budget += money

    if budget <= M:
        start = mid + 1

    else:
        end = mid - 1

print(mid)