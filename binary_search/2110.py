import sys
input = sys.stdin.readline

N, C = map(int, input().split())
answer = 0

houses = [0 for _ in range(N)]

for i in range(N):
    houses[i] = int(input().rstrip())

houses.sort()

start = 1
end = houses[-1]

while (start <= end):
    mid = (start + end) // 2
    count = 1
    current = houses[0]

    for i in range(1, len(houses)):
        if houses[i] >= mid + current:
            count += 1
            current = houses[i]

    if count >= C:
        answer = mid
        start = mid + 1

    else:
        end = mid - 1

print(answer)