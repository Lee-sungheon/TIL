# 창용 마을 무리의 개수
def dfs(v):
    visited[v] = 1
    for u in range(1, N+1):
        if visited[u] == 0 and matrix[v][u] == 1:
            dfs(u)


T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    visited = [0]*(N+1)
    matrix = [[0]*(N+1) for _ in range(N+1)]
    for _ in range(M):
        s, e = map(int, input().split())
        matrix[s][e] = 1
        matrix[e][s] = 1
    cnt = 0
    for i in range(1, N+1):
        if visited[i] == 0:
            dfs(i)
            cnt += 1
    print(f'#{tc+1} {cnt}')