# 캐슬 디펜스
from copy import deepcopy


def combinations(v, s, res):
    if v == m:
        result.append(tuple(res))
    else:
        for i in range(s, n):
            res[v] = i
            combinations(v + 1, i + 1, res)


def bfs(re, dis):
    global kill
    delta = [[-1, -1], [0, 1], [1, -1]]
    for i in range(N):
        for k in range(1, dis+1):
            for j in range(3):
                # if abs(re[j]) == k:
        del matrix[N-i-1]


N, M, D = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
kill = 0

n = M
m = 3
result = []
res = [0]*3
combinations(0, 0, res)
print(result)

for re in result:
    bfs(re, D)

print(matrix)