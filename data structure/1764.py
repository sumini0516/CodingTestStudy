import sys

input = sys.stdin.readline

N, M = map(int, input().split(" "))
arr1 = dict()
list2 = list()

for i in range(N):
    name = input().rstrip()
    arr1[name] = 0

for i in range(M):
    name = input().rstrip()
    if name in arr1:
        list2.append(name)

list2.sort()
print(len(list2))
for name in list2:
    print(name)