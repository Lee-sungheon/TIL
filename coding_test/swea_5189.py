# 전자카트
def dfs(x, cnt, total):
    global result
    if cnt == N-1:
        total += array[x][0]
        if total < result:
            result = total
        return
    if total > result:
        return
    for i in range(N):
        if array[x][i] != 0 and visited[i] == 0:
            visited[i] = 1
            dfs(i, cnt+1, total + array[x][i])
            visited[i] = 0


T = int(input())
for tc in range(T):
    N = int(input())
    result = 10000000000
    array = [list(map(int, input().split())) for _ in range(N)]
    visited = [0]*(N)
    visited[0] = 1
    dfs(0, 0, 0)
    print('#{} {}' .format(tc+1, result))