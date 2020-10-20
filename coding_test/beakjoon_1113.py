# 수영장 만들기
def is_range(r, c):
    if r < 0 or c < 0 or r >= N or c >= M:
        return 0
    return 1


def bfs(r, c, h):
    q = []
    is_con = True
    q.append([r, c])
    total = h - pool[r][c]
    tmp_li = [[r, c]]
    while q:
        tmp = q.pop(0)
        for dx, dy in delta:
            x, y = tmp[1] + dx, tmp[0] + dy
            if not is_range(y, x):
                is_con = False
                continue
            if pool[y][x] < h and not visited[y][x]:
                visited[y][x] = 1
                total += h - pool[y][x]
                tmp_li.append([y, x])
                q.append([y, x])
        if not q and is_con and tmp not in memory:
            memory.extend(tmp_li)
            return total
    return 0


delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]
N, M = map(int, input().split())
pool = [list(map(int, input())) for _ in range(N)]
result = 0
memory = []
for height in range(9, 0, -1):
    visited = [[0]*M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if pool[i][j] < height and not visited[i][j]:
                visited[i][j] = 1
                result += bfs(i, j, height)
print(result)