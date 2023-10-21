import sys
input = sys.stdin.readline

T = int(input())

for i in range(T):
    ans = list()
    N = int(input())
    see = list(map(int, input().split(" ")))
    see.sort()
    M = int(input())
    find = list(map(int, input().split(" ")))

    for i in find:
        start = 0
        end = len(see) - 1
        answer = 0
        while start <= end:
            mid = (start + end) // 2
            if see[mid] == i:
                answer = 1
                break
            elif see[mid] < i:
                start = mid + 1
            else:
                end = mid - 1
        ans.append(answer)
    for i in ans:
        print(i)