# 최소 비용
from collections import deque

delta = ((-1, 0), (0, -1), (1, 0), (0, 1))
T = int(input())
for tc in range(T):
    N = int(input())
    h = [list(map(int, input().split())) for _ in range(N)]
    q = deque()
    q.append((0, 0))
    distance = [[100001]*N for _ in range(N)]
    distance[0][0] = 0
    while q:
        x, y = q.popleft()
        for dx, dy in delta:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N:
                tmp = 1
                if h[y][x] < h[ny][nx]:
                    tmp += (h[ny][nx] - h[y][x])
                if distance[ny][nx] > distance[y][x] + tmp:
                    distance[ny][nx] = distance[y][x] + tmp
                    q.append((nx, ny))
    print('#{} {}' .format(tc+1, distance[-1][-1]))