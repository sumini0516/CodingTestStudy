import sys

# N개의 자연수 중 x, y, z 3개의 수를 뽑아서 x+y+z인 d가 N개의 포함되는 경우 중 가장 큰 d를 찾아라
# x+y+z=d > x+y=d-z

input = sys.stdin.readline

res = 0  #가장 큰 D
N = int(input())
arr = [int(input()) for _ in range(N)]
arr.sort()
arr2 = list()

for i in range(N):
    for j in range(i, N):
        arr2.append(arr[i] + arr[j])

arr2.sort()
#print(arr2)

for i in range(N):
    for j in range(i, N):
        num = arr[j] - arr[i] #x+y 찾기
        start = 0
        end = len(arr2) - 1
        while start <= end:
            mid = (start + end) // 2
            if num > arr2[mid]:
                start = mid + 1
            elif num < arr2[mid]:
                end = mid - 1
            else:
                res = max(res, arr[j])
                break

print(res)
