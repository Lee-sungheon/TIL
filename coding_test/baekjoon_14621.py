# 나만 안되는 연애(MST)
import sys
from heapq import *

input = sys.stdin.readline


def prim(start):
    tree_set = {start}
    q = []
    for edge in graph[start]:
        heappush(q, edge)
    while q:
        weight, x = heappop(q)
        if x not in tree_set:
            tree_set.add(x)
            mst.append((weight, x))
            for edge in graph[x]:
                heappush(q, edge)
    return


def calc(mst):
    res = 0
    for edge in mst:
        res += edge[0]
    return res


v, e = map(int, input().split())
MW = list(input().split())
graph = [[] for _ in range(v+1)]
mst = []
for _ in range(e):
    a, b, c = map(int, input().split())
    if MW[a-1] != MW[b-1]:
        graph[a].append([c, b])
        graph[b].append([c, a])
prim(1)
if len(mst) != v-1:
    print(-1)
else:
    print(calc(mst))
