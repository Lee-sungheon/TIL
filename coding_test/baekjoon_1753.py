# 최단경로 (다익스트라)

from heapq import heappop, heappush
import sys

input = sys.stdin.readline

def di(idx):
    queue = []
    K_distance = [float('inf')] * (V+1)
    K_distance[idx] = 0
    heappush(queue, (0, idx))
    while queue:
        s_cost, s = heappop(queue)
        if K_distance[s] < s_cost:
            continue
        for e, e_cost in distance[s]:
            if K_distance[e] > s_cost + e_cost:
                K_distance[e] = s_cost + e_cost
                heappush(queue, (K_distance[e], e))
    return K_distance


V, E = map(int, input().split())
K = int(input())
distance = [[] for _ in range(V+1)]
for _ in range(E):
    x, y, z = map(int, input().split())
    distance[x].append([y, z])
for i in di(K)[1:]:
    if i == float('inf'):
        print("INF")
    else:
        print(i)