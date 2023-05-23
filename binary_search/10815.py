import sys

input = sys.stdin.readline

def binary_search(i):
    start = 0
    end = N - 1
    while start <= end:
        mid = (start + end) // 2
        if card[mid] == i:
            return 1
        elif card[mid] < i:
            start = mid + 1
        else:
            end = mid - 1
    return 0

N = int(input())

card = list(map(int, input().split(" ")))

# 이분탐색 하기 전 정렬
card.sort()

M = int(input())
target = list(map(int, input().split(" ")))

for i in target:
    print(binary_search(i), end = " ")
