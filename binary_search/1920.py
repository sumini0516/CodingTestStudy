def binary(target):
    left = 0
    right = n - 1
    while left <= right:
        mid = (left + right) // 2
        if n_list[mid] == target:
            return 1
        if n_list[mid] < target:
            left = mid + 1
        elif n_list[mid] > target:
            right = mid - 1


n = int(input())
n_list = list(map(int, input().split(' ')))
n_list.sort()
m = int(input())
list_m = list(map(int, input().split(' ')))
for t in list_m:
    if binary(t) == 1:
        print(1)
    else:
        print(0)
