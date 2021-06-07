# 녹색 옷 입은 애가 젤다지? (다익스트라)

from heapq import heappop, heappush
import sys

input = sys.stdin.readline

def di():
    q = []
    dis = [[float('inf')] * (N) for _ in range(N)]
    dis[0][0] = array[0][0]
    heappush(q, (array[0][0], 0, 0))
    while q:
        s_cost, x, y = heappop(q)
        for dx, dy in delta:
            nx = x + dx
            ny = y + dy
            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue
            if dis[ny][nx] > dis[y][x] + array[ny][nx]:
                dis[ny][nx] = dis[y][x] + array[ny][nx]
                heappush(q, (dis[ny][nx], nx, ny))
    return dis


tc = 1
delta = [(0, 1), (0, -1), (1, 0), (-1, 0)]
while True:
    N = int(input())
    if N == 0:
        break
    array = [list(map(int, input().split())) for _ in range(N)]
    print(f'Problem {tc}: {di()[-1][-1]}')
    tc += 1