# 학교탐방하기 (MST)

import sys
from heapq import *

input = sys.stdin.readline


def prim(start, plus):
    visited = [False] * (v+1)
    result = 0
    visited[start] = 1
    q = [(edge[0]*plus, edge[1]) for edge in graph[start]]
    heapify(q)
    while q:
        weight, x = heappop(q)
        if not visited[x]:
            visited[x] = True
            result += weight
            for edge in graph[x]:
                if not visited[edge[1]]:
                    heappush(q, (edge[0]*plus, edge[1]))
    return result


v, e = map(int, input().split())
graph = [[] for _ in range(v+1)]
for _ in range(e+1):
    a, b, c = map(int, input().split())
    graph[a].append((1^c, b))
    graph[b].append((1^c, a))
print(prim(0, -1)**2 - prim(0, 1)**2)