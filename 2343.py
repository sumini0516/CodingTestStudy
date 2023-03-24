import sys

N, M = map(int, input().split())
course = []
course = list(map(int, input().split()))
start = max(course)
end = 1000000

while (start <= end):
    mid = (start + end) // 2
    blueray_len = 0
    num = 1
    for i in course:
        blueray_len += i
        if blueray_len > mid:
            num += 1
            blueray_len = i
    # print("num", num)
    if num > M:
        # print("start", start, "mid", mid, "end", end)
        start = mid + 1
    else:
        # print("start", start, "mid", mid, "end", end)
        end = mid - 1

print(start)