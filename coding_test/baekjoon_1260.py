# DFS와 BFS
from collections import deque

def dfs(v):
    visited = [0] * (N + 1)
    visited[v] = 1
    stack = [v]
    print(f'{v} ', end='')
    while stack:
        v = stack[-1]
        visited[v] = 1
        for i in range(1, N+1):
            if matrix[v][i] != 0 and visited[i] == 0:
                print(f'{i} ', end='')
                stack.append(i)
                break
        else:
            stack.pop()
    print()

    # for i in range(1, N+1):
    #     if matrix[v][i] != 0 and visited[i] == 0:
    #         dfs(i)


def bfs(V):
    visited = [0] * (N + 1)
    visited[V] = 1
    queue = deque()
    queue.append(V)
    print(f'{V} ', end='')
    while queue:
        q = queue.popleft()
        for i in range(1, N+1):
            if matrix[q][i] != 0 and visited[i] == 0:
                visited[i] = 1
                print(f'{i} ', end='')
                queue.append(i)
    print()


N, M, V = map(int, input().split())
matrix = [[0]*(N+1) for _ in range(N+1)]
for i in range(M):
    x, y = map(int, input().split())
    matrix[x][y] = 1
    matrix[y][x] = 1
dfs(V)
bfs(V)