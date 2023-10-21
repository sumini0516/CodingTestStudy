import sys

input = sys.stdin.readline

N, M = map(int, input().split(" "))
words = dict()

for i in range(N):
    word = input().rstrip()
    if len(word) >= M:
        if word in words:
            words[word] += 1
        else:
            words[word] = 1

answer = sorted(words, key = lambda x : (-words[x], -len(x), x))
print(answer)