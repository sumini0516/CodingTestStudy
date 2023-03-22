import sys

K, N = map(int, input().split())
line = []
line = [int(sys.stdin.readline()) for _ in range(K)]
line.sort()  # 539, 457, 743, 802
start = 1
end = max(line)
while (start <= end):
    mid = (start + end) // 2
    num = 0
    for i in line:
        num += i // mid
    if num >= N:
        start = mid + 1
    else:
        end = mid - 1

print(end)
