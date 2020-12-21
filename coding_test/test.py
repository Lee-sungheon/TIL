from collections import defaultdict, deque
import sys


def bfs(D):
    global max_cnt
    res = 0
    S = deque([D])
    visit[D] = False
    while S:
        res += 1
        tmp = S.popleft()
        for i in dic[tmp]:
            if visit[i]:
                S.append(i)
                visit[i] = False
    if max_cnt < res:
        L.clear()
        L.append(D)
        max_cnt = res
    elif max_cnt == res:
        L.append(D)
    return


input = sys.stdin.readline

N, M = map(int, input().split())
L = []
max_cnt = 0
dic = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    dic[b].append(a)

for key in range(len(dic)):
    if dic[key]:
        visit = [True] * (N+1)
        bfs(key)

for i in L:
    print(i, end=' ')