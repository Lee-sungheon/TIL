# 비상구 탈출

t = int(input())
for tc in range(t):
    n = int(input())
    factory = [list(map(int, input().split())) for _ in range(n)]
    E = []
    dis = [[], []]
    for i in range(n):
        for j in range(n):
            if factory[i][j] == 2:
                E.append([i, j])
    for i in range(n):
        for j in range(n):
            if factory[i][j] == 1:
                dis[0].append(abs(i - E[0][0]) + abs(j - E[0][1]))
                dis[1].append(abs(i - E[1][0]) + abs(j - E[1][1]))
    N = len(dis[0])
    visit = [False] * N
    result = []
    print(dis)
    while True:
        diff = []
        for i in range(N):
            if not visit[i]:
                diff.append(dis[0][i]-dis[1][i])
        a, b = min(diff), max(diff)
        idx = 0
        if a >= 0 and b >= 0:
            idx = 1
        min_val = 1000
        for i in range(N):
            if min_val > dis[idx][i] and not visit[i]:
                min_val = dis[idx][i]

        tmp = []
        for i in range(N):
            if dis[idx][i] == min_val and not visit[i]:
                tmp.append([dis[(idx+1) % 2][i] - dis[idx][i], i])
        tmp.sort(reverse=True)
        if tmp[0][0] >= 0:
            visit[tmp[0][1]] = True
            for i in range(N):
                if dis[idx][i] == min_val:
                    dis[idx][i] += 1
        result.append(min_val+1)
        if visit.count(False) == 0:
            break
    print('#{} {}' .format(tc+1, max(result)))

# 5
# 5
# 0 0 1 0 1
# 0 0 0 2 0
# 0 0 0 0 0
# 0 0 1 0 1
# 0 0 2 0 0
# 6
# 0 0 1 0 0 0
# 0 2 1 0 0 0
# 1 1 1 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 2 1
# 0 0 0 0 1 1
# 7
# 0 0 0 0 0 0 0
# 0 0 0 1 0 2 0
# 0 0 0 1 0 0 0
# 0 1 1 1 1 1 0
# 0 0 0 1 0 0 0
# 0 2 0 1 0 0 0
# 0 0 0 0 0 0 0
# 10
# 2 0 0 0 0 0 0 0 0 0
# 0 2 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 1
# 0 0 0 0 0 0 0 0 1 1
# 0 0 0 0 0 0 0 1 1 1
# 0 0 0 0 0 0 1 1 1 1
# 10
# 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 1 0 0
# 0 0 0 0 1 1 0 0 0 0
# 0 0 0 0 0 0 0 0 1 0
# 0 0 1 0 0 2 0 0 0 0
# 0 0 1 0 0 0 1 1 0 0
# 0 0 0 2 0 0 0 0 0 0
# 0 0 0 0 0 1 0 0 0 0
# 0 0 0 1 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0
