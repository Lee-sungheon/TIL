# 나는야 포켓몬 마스터 이다솜

import sys

input = sys.stdin.readline
N, M = map(int, input().split())
dic1 = dict()
dic2 = dict()
for i in range(1, N+1):
    name = input().strip()
    dic1[str(i)] = name
    dic2[name] = str(i)

for _ in range(M):
    question = input().strip()
    if '1' <= question[:1] <= '9':
        print(dic1[question])
    else:
        print(dic2[question])