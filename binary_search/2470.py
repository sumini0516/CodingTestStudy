import sys

input = sys.stdin.readline

N = int(input())
liquid = list(map(int, input().split(" ")))
liquid.sort()

start = 0
end = N - 1

answer = abs(liquid[start] + liquid[end])
liquid_answer = [liquid[start], liquid[end]]

while start < end:
    ans = liquid[start] + liquid[end]
    if abs(ans) <= answer:
        liquid_answer = [liquid[start], liquid[end]]
        answer = abs(ans)
    if ans < 0:
        start += 1
    else:
        end -= 1

liquid_answer.sort()

for i in liquid_answer:
    print(i, end = " ")