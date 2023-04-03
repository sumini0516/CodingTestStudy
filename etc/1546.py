import math


def new_scores(x):
    return x / max_score * 100

n = int(input())
scores = list(map(int, input().split()))
max_score = max(scores)
new_scores = list(map(new_scores(), scores))
print(sum(new_scores))
