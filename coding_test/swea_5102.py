def bfs(S):
    visited = [0]*(V+1)
    queue = [(S, 0)]
    visited[S] = 1
    while queue:
        s, cnt = queue.pop(0)
        if s == G:
            return cnt
        for e in range(V+1):
            if matrix[s][e] != 0 and visited[e] == 0:
                queue.append((e, cnt + 1))
                visited[s] = 1
    return 0


T = int(input())
for tc in range(T):
    V, E = map(int, input().split())
    matrix = [[0]*(V+1) for _ in range(V+1)]
    for _ in range(E):
        x, y = map(int, input().split())
        matrix[x][y] = 1
        matrix[y][x] = 1
    S, G = map(int, input().split())
    print(f'#{tc+1} {bfs(S)}')
