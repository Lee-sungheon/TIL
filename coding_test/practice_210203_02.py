# 도로 건설

t = int(input())
for tc in range(t):
    W, H = map(int, input().split())
    map_li = [list(map(int, input().split())) for _ in range(H)]
    road = []
    # 가로 확인
    for i in range(H):
        if map_li[i].count(1) == 0:
            road.append([[i, j] for j in range(W)])
    # 세로 확인
    for j in range(W):
        for i in range(H):
            if map_li[i][j] == 1:
                break
        else:
            road.append([[k, j] for k in range(H)])
    # 대각 확인
    for i in range(H-1):
        tmp = []
        for j in range(H-i):
            if j + i >= H or j >= W:
                continue
            if map_li[j+i][j] == 1:
                break
            tmp.append([j+i, j])
        else:
            road.append(tmp)

    for i in range(W-1):
        tmp = []
        for j in range(W-i):
            if j + i >= W or j >= H:
                continue
            if map_li[j][j+i] == 1:
                break
            tmp.append([j, j+i])
        else:
            road.append(tmp)

    for i in range(H-1):
        tmp = []
        for j in range(H-i):
            if H-(j+i)-1 < 0 or j >= W:
                continue
            if map_li[H-(j+i)-1][j] == 1:
                break
            tmp.append([H-(j+i)-1, j])
        else:
            road.append(tmp)

    for i in range(W-1):
        tmp = []
        for j in range(W-i):
            if H-(j+i)-1 < 0 or j >= H:
                continue
            if map_li[j][W-(j+i)-1] == 1:
                break
            tmp.append([j, W-(j+i)-1])
        else:
            road.append(tmp)

    if not road:
        print('#{} -1' .format(tc+1))
    else:
        homes = []
        min_val = 1000
        for i in range(H):
            for j in range(W):
                if map_li[i][j] == 1:
                    homes.append([i, j])

        for ro in road:
            home_min = [1000] * len(homes)
            for i in range(len(homes)):
                for j in range(len(ro)):
                    dis = abs(homes[i][0] - ro[j][0]) + abs(homes[i][1] - ro[j][1])
                    if dis < home_min[i]:
                        home_min[i] = dis
            if min_val > max(home_min):
                min_val = max(home_min)
        print('#{} {}'.format(tc + 1, min_val))
