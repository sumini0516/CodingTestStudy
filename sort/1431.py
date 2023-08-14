import sys

input = sys.stdin.readline

def compare(inputs):
    ans = 0
    for i in inputs:
        if i.isdigit():
            ans += int(i)
    return ans

num = list()
N = int(input())

for i in range(N):
    M = input().rstrip()
    num.append(M)

num.sort(key = lambda x : (len(x), compare(x), x))

for i in num:
    print(i)