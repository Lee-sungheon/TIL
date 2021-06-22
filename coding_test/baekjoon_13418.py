# 학교탐방하기 (MST)

import sys
from heapq import *

input = sys.stdin.readline


def prim(start):
    q = []
    result = 0
    visited[start] = 1
    for edge in graph[start]:
        heappush(q, edge)
    while q:
        weight, x = heappop(q)
        if visited[x] == 0:
            visited[x] = 1
            result += weight
            for edge in graph[x]:
                heappush(q, edge)
    return result


v, e = map(int, input().split())
graph = [[] for _ in range(v+1)]
visited = [0] * (v+1)
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append([1-c, b])
    graph[b].append([1-c, a])
value1 = prim(0)**2
for i in range(len(graph)):
    for j in range(len(graph[i])):
        graph[i][j][0] -= 1
visited = [0] * (v+1)
value2 = prim(0)**2
print(value2 - value1)