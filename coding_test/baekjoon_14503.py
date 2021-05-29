# 로봇 청소기
from sys import stdin
input = stdin.readline

delta = [(-1, 0), (0, -1), (1, 0), (0, 1)]
rotation = {0: 3, 3: 2, 2: 1, 1: 0}
back = [(0, 1), (-1, 0), (0, -1), (1, 0)]
N, M = map(int, input().split())
r, c, d = map(int, input().split())
rooms = [list(map(int, input().split())) for _ in range(N)]
cnt = 0

while True:
    if rooms[r][c] == 0:
        rooms[r][c] = 2
        cnt += 1
    dx, dy = delta[d]
    if rooms[r+dy][c+dx] == 0:
        r += dy
        c += dx
        d = rotation[d]
    elif rooms[r+1][c] >= 1 and rooms[r-1][c] >= 1 and rooms[r][c+1] >= 1 and rooms[r][c-1] >= 1:
        bx, by = back[d]
        if rooms[r+by][c+bx] == 2:
            r += by
            c += bx
            continue
        else:
            break
    elif rooms[r+dy][c+dx] >= 1:
        d = rotation[d]
print(cnt)