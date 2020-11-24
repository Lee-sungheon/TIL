# 전기버스2

def dfs(cnt, k, bat):
    global result
    bat -= 1
    if bat < 0:
        return
    if k >= N-1:
        result = min(result, cnt)
        return
    if cnt >= result:
        return
    dfs(cnt+1, k+1, M[k])
    dfs(cnt, k+1, bat)


T = int(input())
for tc in range(T):
    M = list(map(int, input().split()))
    N = M.pop(0)
    result = 1000
    dfs(0, 1, M[0])
    print('#{} {}' .format(tc+1, result))