# 최소 스패닝 트리
import sys
from heapq import *


def prim(start):
    tree_set = {start}
    q = graph[start]
    while q:
        weight, x1, x2 = heappop(q)
        if x2 not in tree_set:
            tree_set.add(x2)
            mst.append((weight, x1, x2))
            for edge in graph[x2]:
                heappush(q, edge)
    return


def calc(mst):
    res = 0
    for edge in mst:
        res += edge[0]
    return res


v, e = map(int, sys.stdin.readline().split())
graph = {i: [] for i in range(1, v+1)}
mst = []
for _ in range(e):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((c, a, b))
    graph[b].append((c, b, a))
print(graph)
prim(1, graph)
print(mst)
