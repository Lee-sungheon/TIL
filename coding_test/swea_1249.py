# 보급로
from collections import deque
import heapq

delta = ((-1, 0), (0, -1), (1, 0), (0, 1))
T = int(input())
for tc in range(T):
    N = int(input())
    h = [list(map(int, input())) for _ in range(N)]
    q = []
    distance = [[100001]*N for _ in range(N)]
    distance[0][0] = 0
    heapq.heappush(q, [distance[0][0], [0, 0]])
    while q:
        tmp = heapq.heappop(q)
        x, y = tmp[1][0], tmp[1][1]
        for dx, dy in delta:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N:
                if distance[ny][nx] > distance[y][x] + h[ny][nx]:
                    distance[ny][nx] = distance[y][x] + h[ny][nx]
                    heapq.heappush(q, [distance[ny][nx], [nx, ny]])
    print('#{} {}' .format(tc+1, distance[-1][-1]))