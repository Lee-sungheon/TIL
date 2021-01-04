# 유기농 배추(dfs)
import sys
sys.setrecursionlimit(10**5)


def dfs(x, y):
    delta = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    for dx, dy in delta:
        nx = x + dx
        ny = y + dy
        if nx < 0 or ny < 0 or nx >= M or ny >= N:
            continue
        if matrix[ny][nx] == 1:
            matrix[ny][nx] = 0
            dfs(nx, ny)


t = int(input())
for _ in range(t):
    M, N, K = map(int, input().split())
    matrix = [[0]*M for _ in range(N)]
    result = 0
    for i in range(K):
        x, y = map(int, input().split())
        matrix[y][x] = 1
    for i in range(N):
        for j in range(M):
            if matrix[i][j] == 1:
                result += 1
                matrix[i][j] = 0
                dfs(j, i)
    print(result)