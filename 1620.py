# 1번인 포켓몬부터 N번에 해당하는 포켓몬까지 한 줄에 하나씩 입력
# 포켓몬의 이름은 모두 영어 (대문자 + 소문자, 소문자 + 대문자)
# 2 <= 이름의 길이 <= 20
# M개의 줄에 맞춰야 하는 문제가 입력으로 들어옴
# 알파벳 > 포켓몬 번호, 숫자 > 포켓몬 문자
import sys

N, M = map(int, input().split())
pocket = {}

for i in range(N):
    name = sys.stdin.readline().rstrip()
    pocket[i + 1] = name
    pocket[name] = i + 1

for i in range(M):
    find_pocket = sys.stdin.readline().rstrip()
    if find_pocket.isdigit():
        print(pocket[int(find_pocket)])
    else:
        print(pocket[find_pocket])