# 파티 (다익스트라)

import heapq
import sys

def di(dis):
    queue = []
    K_distance = [INF for _ in range(N + 1)]
    K_distance[X] = 0
    heapq.heappush(queue, [0, X])
    while queue:
        mid = heapq.heappop(queue)
        if K_distance[mid[1]] < mid[0]:
            continue
        for end in dis[mid[1]]:
            if K_distance[end[0]] > mid[0] + end[1]:
                K_distance[end[0]] = mid[0] + end[1]
                heapq.heappush(queue, [K_distance[end[0]], end[0]])
    return K_distance


input = sys.stdin.readline

N, M, X = map(int, input().split())
distance = [[] for _ in range(N+1)]
distance2 = [[] for _ in range(N+1)]
INF = 100 * M + 1
result = []
for _ in range(M):
    x, y, z = map(int, input().split())
    distance[x].append([y, z])
    distance2[y].append([x, z])
K_distance = di(distance)
K_distance_home = di(distance2)
max_val = 0
for i in range(1, N+1):
    if max_val < K_distance_home[i] + K_distance[i]:
        max_val = K_distance_home[i] + K_distance[i]
print(max_val)
