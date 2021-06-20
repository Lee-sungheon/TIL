# 학교탐방하기 (MST)

import sys
from heapq import *

input = sys.stdin.readline


def prim(start):
    tree_set = {start}
    q = []
    result = 0
    for edge in graph[start]:
        heappush(q, edge)
    while q:
        weight, x = heappop(q)
        if x not in tree_set:
            tree_set.add(x)
            result += weight
            for edge in graph[x]:
                heappush(q, edge)
    return result


v, e = map(int, input().split())
graph = [[] for _ in range(v+1)]
value1 = 0
for _ in range(e):
    a, b, c = map(int, input().split())
    if c == 0:  c = 1
    else:  c = 0
    graph[a].append([c, b])
    graph[b].append([c, a])
value1 = prim(0)**2
for i in range(len(graph)):
    for j in range(len(graph[i])):
        if graph[i][j][0] == 1:
            graph[i][j][0] = 0
        else:
            graph[i][j][0] = -1
value2 = prim(0)**2
print(value2 - value1)