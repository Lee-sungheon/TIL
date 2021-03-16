# 미로에 갇힌 건우
from collections import deque

delta = [[0, 1], [0, -1], [1, 0], [-1, 0]]


def bfs():
    q = deque()
    q.append([[0, 0], 0])
    sun_visited = [[False] * n for _ in range(n)]
    moon_visited = [[False] * n for _ in range(n)]
    while q:
        tmp = q.popleft()
        x, y = tmp[0]
        bfs_m = tmp[1]+1
        print(tmp)
        if x == y == n-1:
            return bfs_m
        if m <= (bfs_m-1)%(2*m) < m*2:
            for dx, dy in delta:
                nx, ny = x + dx, y + dy
                if nx < 0 or ny < 0 or nx >= n or ny >= n:
                    continue
                if maze[ny][nx] == 0 and not moon_visited[ny][nx]:
                    moon_visited[ny][nx] = True
                    q.append([[nx, ny], bfs_m])
                elif maze[ny][nx] == 1 and not moon_visited[ny][nx]:
                    while True:
                        nx, ny = nx + dx, ny + dy
                        if nx < 0 or ny < 0 or nx >= n or ny >= n:
                            break
                        if maze[ny][nx] == 1:
                            continue
                        elif maze[ny][nx] == 0:
                            q.append([[nx, ny], bfs_m])
                            moon_visited[ny][nx] = True
                            break
        else:
            for dx, dy in delta:
                nx, ny = x + dx, y + dy
                if nx < 0 or ny < 0 or nx >= n or ny >= n:
                    continue
                if maze[ny][nx] == 0 and not sun_visited[ny][nx]:
                    sun_visited[ny][nx] = True
                    q.append([[nx, ny], bfs_m])
                elif maze[ny][nx] == 1:
                    continue
    return -1


n, m = map(int, input().split())
maze = [list(map(int, input().split())) for _ in range(n)]
result = bfs()
day = (result//(m*2))+1
if 0 <= (result-1)%(m*2) < m:
    sunormoon = 'sun'
else:
    sunormoon = 'moon'
if result == -1:
    print(result)
else:
    print('{} {}' .format(day, sunormoon))
