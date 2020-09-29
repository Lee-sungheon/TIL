# 길 찾기
for _ in range(10):
    def dfs(v):
        visited[v] = 1
        for w in range(1, N+1):
            if G[v][w] == 1 and visited[w] == 0:
                dfs(w)

    tc, E = map(int, input().split())
    N = 99
    temp = list(map(int, input().split()))
    G = [[0] * (N+1) for _ in range(N+1)]
    visited = [0] * (N+1)

    for i in range(E):
        s, e = temp[2*i], temp[2*i+1]
        G[s][e] = 1

    dfs(1)
    if visited[99] == 1:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')