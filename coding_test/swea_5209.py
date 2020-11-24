# 최소 생산 비용
def dfs(dep, total):
    global result
    if dep == N:
        result = min(result, total)
        return
    if total >= result:
        return
    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            dfs(dep+1, total + array[dep][i])
            visited[i] = 0


T = int(input())
for tc in range(T):
    N = int(input())
    array = [list(map(int, input().split())) for _ in range(N)]
    visited = [0]*N
    result = 100000000
    dfs(0, 0)
    print('#{} {}' .format(tc+1, result))