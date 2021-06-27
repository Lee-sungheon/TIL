# 도시 분할 계획 (mst)

import sys
from heapq import *

input = sys.stdin.readline


def prim(start):
    visited = [False] * (v + 1)
    result = 0
    visited[start] = 1
    max_val = 0
    q = []
    cnt = 0
    for edge in graph[start]:
        heappush(q, edge)
    while q:
        weight, x = heappop(q)
        if not visited[x]:
            visited[x] = True
            cnt += 1
            result += weight
            if weight > max_val:
                max_val = weight
            for edge in graph[x]:
                if not visited[edge[1]]:
                    heappush(q, edge)
        if cnt >= v-1:
            break
    return result - max_val


v, e = map(int, input().split())
graph = [[] for _ in range(v+1)]
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))
    graph[b].append((c, a))
print(prim(1))