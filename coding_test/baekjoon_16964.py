# DFS 스페셜 저지
import sys


def dfs(x):
    visited[x] = True
    result.append(x)
    for y in matrix[x]:
        if not visited[y]:
            dfs(y)


input = sys.stdin.readline
N = int(input())
matrix = [[] for _ in range(N+1)]
for i in range(N - 1):
    a, b = map(int, input().split())
    matrix[a].append(b)
    matrix[b].append(a)
order = list(map(int, input().split()))
res = [0] * (N+1)
for i in range(1, N+1):
    res[order[i-1]] = i
for i in matrix:
    i.sort(key=lambda x: res[x])
visited = [False] * (N + 1)
result = []
dfs(1)
if result == order:
    print(1)
else:
    print(0)
