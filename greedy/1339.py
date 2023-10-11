import sys

input = sys.stdin.readline

N = int(input().rstrip())
alpha = list()
num_alpha = list()
alpha_dict = dict()
sorted_list = list()

for i in range(N):
    M = input().rstrip()
    alpha.append(M)
    for j in range(len(M)):
        A = M[j]
        if A not in alpha_dict:
            alpha_dict[A] = (10 ** (len(M) - j - 1))
        else:
            alpha_dict[A] += (10 ** (len(M) - j - 1))

alpha_sort = sorted(alpha_dict, key = lambda x : (-alpha_dict[x]))
# print(alpha_sort)
for i in alpha:
    K = ""
    for j in i:
        K += str(9 - alpha_sort.index(j))
    num_alpha.append(int(K))

# print(alpha_dict)
# print(alpha_sort)
print(sum(num_alpha))