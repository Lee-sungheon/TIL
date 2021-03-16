# 민준이와 마산 그리고 건우
import heapq
import sys

input = sys.stdin.readline

def dijkstra(p):
    queue = []
    K_distance = [INF for _ in range(V + 1)]
    K_distance[p] = 0
    heapq.heappush(queue, [0, p])
    while queue:
        mid = heapq.heappop(queue)
        for end in distance[mid[1]]:
            if K_distance[end[0]] > mid[0] + end[1]:
                K_distance[end[0]] = mid[0] + end[1]
                heapq.heappush(queue, [K_distance[end[0]], end[0]])
    return [K_distance[-1], K_distance[P]]


V, E, P = map(int, input().split())
INF = 100000000 * V + 1
distance = [[] for _ in range(V + 1)]
for _ in range(E):
    start, end, dist = map(int, input().split())
    distance[start].append([end, dist])
    distance[end].append([start, dist])
min_val, val = dijkstra(1)
val += dijkstra(P)[0]
if min_val == val:
    print("SAVE HIM")
else:
    print("GOOD BYE")