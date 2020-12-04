import heapq
import sys

N, M, S, E = map(int, sys.stdin.readline().split())
matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]
INF = 2**60
distance = [[] for _ in range(N + 1)]
for i in range(M):
    start, end, dist, t1, t2 = matrix[i]
    distance[start].append([end, dist, t1])
    distance[end].append([start, dist, t2])
queue = []
K_distance = [INF for _ in range(N + 1)]
K_distance[0] = K_distance[1] = 0
heapq.heappush(queue, [0, 1])
visited = [False for _ in range(N + 1)]
while queue:
    mid = heapq.heappop(queue)
    if visited[mid[1]]:
        continue
    visited[mid[1]] = True
    for end in distance[mid[1]]:
        if end[2] == 1 and ((mid[0] <= S < mid[0] + end[1]) or (S <= mid[0] <= E)):
            if mid[0] >= S:
                dis = 0
                en = E - mid[0]
            else:
                dis = S - mid[0]
                en = E - S
            move = end[1] - dis
            if en // 2 >= move:
                dis += move * 2
            else:
                dis += en + (move - en / 2)
            tmp = mid[0] + dis
        else:
            tmp = mid[0] + end[1]
        if K_distance[end[0]] > tmp:
            K_distance[end[0]] = tmp
            heapq.heappush(queue, [K_distance[end[0]], end[0]])
for i in range(N + 1):
    if K_distance[i] % 1 == 0:
        K_distance[i] = int(K_distance[i])
print(max(K_distance))