# 정사각형 방
def bfs(x, y):
    queue = [[(x, y), 1]]
    delta = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    count = 0
    while queue:
        tmp = queue.pop(0)
        x = tmp[0][0]
        y = tmp[0][1]
        cnt = tmp[1]
        for dx, dy in delta:
            nx = x + dx
            ny = y + dy
            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue
            elif A[y][x] + 1 == A[ny][nx]:
                queue.append([(nx, ny), cnt + 1])
            if cnt >= count:
                count = cnt
    return count


T = int(input())
for tc in range(T):
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]
    room_cnt = []
    for i in range(N):
        for j in range(N):
            room_cnt.append(((bfs(j, i)), -A[i][j]))
    max_val = max(room_cnt)
    index = room_cnt.index(max_val)
    print(f'#{tc+1} {-max_val[1]} {max_val[0]}')