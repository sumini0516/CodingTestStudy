# N개의 정수로 이루어진 수열이 있을 때, 크기가 양수인 부분수열 중에서 그 수열의 원소를 다 더한 값이 S가 되는 경우의 수를 구하시오
# 탈출조건: 수열의 원소의 합이 S가 되는 경우
# Promising:
import sys

def dfs(idx, res):
    global cnt
    if idx >= n:
        print("x")
        return

    print(k[idx])
    res += k[idx]

    if res == s:
        cnt += 1

    print("1", idx + 1, res)
    dfs(idx + 1, res) #현재 값을 포함해서 구하기
    print("2", idx + 1, res - k[idx])
    print("k[idx]:", k[idx])
    dfs(idx + 1, res - k[idx])


n, s = map(int, sys.stdin.readline().split())
k = list(map(int, sys.stdin.readline().split()))
cnt = 0

dfs(0, 0)
print(cnt)