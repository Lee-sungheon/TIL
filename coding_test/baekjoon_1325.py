# 효율적인 해킹
import sys
from collections import deque

# dfs는 왜 메모리초과가 날까????

# def dfs(x):
#     global value
#     visited[x] = True
#     for y in graph[x]:
#         if not visited[y]:
#             value += 1
#             dfs(y)

def bfs(x):
    val = 0
    q = deque()
    q.append(x)
    visited = [False] * (N+1)
    visited[x] = True
    while q:
        tmp = q.popleft()
        val += 1
        for y in graph[tmp]:
            if not visited[y]:
                visited[y] = True
                q.append(y)
    return val


input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[b].append(a)

max_value = 0
result = []
print(graph)
for i in range(1, N+1):
    if graph[i]:
        value = bfs(i)
        if max_value <= value:
            if max_value < value:
                result = []
            max_value = value
            result.append(i)
print(*result)
