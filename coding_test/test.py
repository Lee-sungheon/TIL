import sys
sys.setrecursionlimit(10**4)


def dfs(x):
    global value
    visited[x] = True
    for y in range(len(graph[x])):
        if not visited[graph[x][y]]:
            value += 1
            dfs(graph[x][y])


input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[b].append(a)
max_value = 0
result = []
for i in range(1, N+1):
    if graph[i]:
        visited = [False]*(N+1)
        value = 1
        dfs(i)
        if max_value <= value:
            if max_value < value:
                result = []
            max_value = value
            result.append(i)
print(*result)