import sys
input = sys.stdin.readline

K, N = map(int, input().split())

lines = [0 for _ in range(K)]

for i in range(K):
    lines[i] = int(input().rstrip())

start = 1
end = 2 ** 31 - 1

while(start <= end):
    mid = (start + end) // 2
    cut_line = 0

    for line in lines:
        if line >= mid:
            cut_line += (line // mid)

    if cut_line >= N:
        start = mid + 1

    else:
        end = mid - 1

print(end)