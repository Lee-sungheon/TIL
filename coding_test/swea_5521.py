# 상원이의 생일파티

T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    matrix = [[0]*(N+1) for _ in range(N+1)]
    visited = [0]*(N+1)
    for i in range(M):
        a, b = map(int, input().split())
        matrix[a][b] = 1
        matrix[b][a] = 1
    for i in range(N+1):
        if matrix[1][i] == 1:
            visited[i] = 1
            for j in range(N+1):
                if matrix[i][j] == 1:
                    visited[j] = 1

    if visited[1] == 1:
        result = visited.count(1) - 1
    else:
        result = visited.count(1)
    print('#{} {}' .format(tc+1, result))
