# 특정한 최단 경로 (다익스트라)

import heapq
import sys

input = sys.stdin.readline


def di(idx):
    queue = []
    K_distance = [INF for _ in range(N + 1)]
    K_distance[idx] = 0
    heapq.heappush(queue, [0, idx])
    while queue:
        mid = heapq.heappop(queue)
        if K_distance[mid[1]] < mid[0]:
            continue
        for end in distance[mid[1]]:
            if K_distance[end[0]] > mid[0] + end[1]:
                K_distance[end[0]] = mid[0] + end[1]
                heapq.heappush(queue, [K_distance[end[0]], end[0]])
    return K_distance


N, E = map(int, input().split())
distance = [[] for _ in range(N+1)]
INF = 1000 * E + 1
for _ in range(E):
    x, y, z = map(int, input().split())
    distance[x].append([y, z])
    distance[y].append([x, z])
v1, v2 = map(int, input().split())

start = di(1)
v1_res = di(v1)
v2_res = di(v2)

res1 = start[v1] + v1_res[v2] + v2_res[-1]
res2 = start[v2] + v2_res[v1] + v1_res[-1]

if res1 >= INF or res2 >= INF:
    print(-1)
else:
    print(min(res1, res2))
