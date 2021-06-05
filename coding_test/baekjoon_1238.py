# 파티 (다익스트라)

import heapq
import sys

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
queue = []
K_distance_home = [INF for _ in range(N+1)]
K_distance_home[X] = 0
heapq.heappush(queue, [0, X])
while queue:
    mid = heapq.heappop(queue)
    for end in distance[mid[1]]:
        if K_distance_home[end[0]] > mid[0] + end[1]:
            K_distance_home[end[0]] = mid[0] + end[1]
            heapq.heappush(queue, [K_distance_home[end[0]], end[0]])
queue = []
K_distance = [INF for _ in range(N+1)]
K_distance[X] = 0
heapq.heappush(queue, [0, X])
while queue:
    mid = heapq.heappop(queue)
    for end in distance2[mid[1]]:
        if K_distance[end[0]] > mid[0] + end[1]:
            K_distance[end[0]] = mid[0] + end[1]
            heapq.heappush(queue, [K_distance[end[0]], end[0]])
max_val = 0
for i in range(1, N+1):
    if max_val < K_distance_home[i] + K_distance[i]:
        max_val = K_distance_home[i] + K_distance[i]
print(max_val)