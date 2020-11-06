# 탈주범 검거
from collections import deque


def bfs(r, c):
    global result
    visited = [[0]*M for _ in range(N)]
    q = deque()
    q.append([(r, c), 1])
    visited[r][c] = 1
    while q:
        tmp = q.popleft()
        r, c = tmp[0][0], tmp[0][1]
        if tmp[1] > L:
            break
        result += 1
        for dr, dc in delta[ter[r][c]]:
            nr, nc = r + dr, c + dc
            if nr < 0 or nc < 0 or nr >= N or nc >= M:
                continue
            if ter[nr][nc] in ter_type[(dr, dc)] and visited[nr][nc] == 0:
                q.append([(nr, nc), tmp[1]+1])
                visited[nr][nc] = 1


ter_type = {(-1, 0): [1, 2, 5, 6], (1, 0): [1, 2, 4, 7], (0, -1): [1, 3, 4, 5], (0, 1): [1, 3, 6, 7]}
delta = ([], [(-1, 0), (1, 0), (0, -1), (0, 1)], [(-1, 0), (1, 0)], [(0, -1), (0, 1)], [(-1, 0), (0, 1)],
         [(1, 0), (0, 1)], [(1, 0), (0, -1)], [(-1, 0), (0, -1)])
T = int(input())
for tc in range(T):
    N, M, R, C, L = map(int, input().split())
    ter = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    bfs(R, C)
    print('#{} {}' .format(tc+1, result))