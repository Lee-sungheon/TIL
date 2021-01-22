# 최소합
def dfs(x, y, total):
    global result
    if x == N-1 and y == N-1:
        if total < result:
            result = total
        return
    if total > result:
        return
    if x+1 < N:
        dfs(x+1, y, total+array[x+1][y])
    if y+1 < N:
        dfs(x, y+1, total+array[x][y+1])


T = int(input())
for tc in range(T):
    result = 1000000000
    N = int(input())
    array = [list(map(int, input().split())) for _ in range(N)]
    dfs(0, 0, array[0][0])
    print('#{} {}' .format(tc+1, result))
