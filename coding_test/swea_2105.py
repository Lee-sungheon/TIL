# [모의 SW 역량테스트] 디저트 카페
def dfs(x, y, cnt):
    global result
    if cnt >= 4:
        if dis[0] == dis[2] and dis[1] == dis[3]:
            tmp_desert = desert[:len(desert)-1]
            if len(tmp_desert) == len(set(tmp_desert)):
                if result < len(tmp_desert):
                    result = len(tmp_desert)
        return

    if cnt >= 3 and dis[0] != dis[2]:
        return

    if len(desert) != len(set(desert)):
        return

    dx, dy = delta[cnt]
    nx, ny = x + dx, y + dy
    if nx < 0 or ny < 0 or nx >= N or ny >= N:
        return
    desert.append(cafe[ny][nx])
    dis[cnt] += 1
    dfs(nx, ny, cnt)
    dfs(nx, ny, cnt+1)
    dis[cnt] -= 1
    desert.pop()


T = int(input())
delta = [[1, 1], [-1, 1], [-1, -1], [1, -1]]
for tc in range(T):
    N = int(input())
    cafe = [list(map(int, input().split())) for _ in range(N)]
    result = -1
    for i in range(N):
        for j in range(N):
            desert = [cafe[i][j]]
            dis = [0, 0, 0, 0]
            dfs(j, i, 0)
    print("#{} {}" .format(tc+1, result))