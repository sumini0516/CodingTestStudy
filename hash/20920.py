import sys

input = sys.stdin.readline

N, M = map(int, input().split(" "))
words = dict()

for i in range(N):
    word = input().rstrip()
    if len(word) >= M:
        if word not in words:
            words[word] = 1
        else:
            words[word] += 1

memory = sorted(words, key = lambda x: (-words[x], -len(x), x))

for i in memory:
    print(i)