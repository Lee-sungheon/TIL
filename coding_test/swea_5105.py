# SWEA_5105

def bfs(x, y):
    visited = [[0]*N for _ in range(N)]
    queue = [[(x, y), 0]]
    delta = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    visited[y][x] = 1
    while queue:
        tmp = queue.pop(0)
        x, y = tmp[0]
        cnt = tmp[1]
        if maze[y][x] == '3':
            return cnt-1
        for dx, dy in delta:
            nx, ny = x + dx, y + dy
            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue
            if maze[ny][nx] != '1' and visited[ny][nx] == 0:
                queue.append([(nx, ny), cnt+1])
                visited[ny][nx] = 1
    return 0


def search():
    for i in range(N):
        for j in range(N):
            if maze[i][j] == '2':
                return bfs(j, i)


T = int(input())
for tc in range(T):
    N = int(input())
    maze = [list(input()) for _ in range(N)]
    print(f'#{tc+1} {search()}')