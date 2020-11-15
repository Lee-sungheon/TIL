# 최적 경로
def dfs(x, y, dep, total):
    global result
    if dep == N:
        total += (abs(x-arr[2]) + abs(y-arr[3]))
        result = min(result, total)
        return

    if total > result:
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            nx, ny = arr[2*(i+2)], arr[2*(i+2)+1]
            dfs(nx, ny, dep+1, total + abs(nx-x) + abs(ny-y))
            visited[i] = 0


T = int(input())
for tc in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    result = 100000
    visited = [0]*2 + [0]*N
    dfs(arr[0], arr[1], 0, 0)
    print('#{} {}' .format(tc+1, result))