import sys

input = sys.stdin.readline

N = int(input())
liquid = list(map(int, input().split(" ")))
liquid.sort()
start = 0
end = len(liquid) - 1
answer = [liquid[start], liquid[end]]
compare = abs(liquid[start] + liquid[end])

while(start < end):
    mid = (start + end) // 2
    compare2 = liquid[start] + liquid[end]
    if abs(compare2) < compare:
        answer = [liquid[start], liquid[end]]
        compare = abs(compare2)
    if mid < 0:
        start = mid + 1
    else:
        end = mid - 1

print(answer[0], answer[1])