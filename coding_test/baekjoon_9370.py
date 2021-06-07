# 미확인 도착지 (다익스트라)
from heapq import heappop, heappush
import sys

input = sys.stdin.readline

def di(idx):
    q = []
    dis = [float('inf')] * (n+1)
    dis[idx] = 0
    heappush(q, (0, idx))
    while q:
        s_cost, s = heappop(q)
        if dis[s] < s_cost:
            continue
        for e, e_cost in graph[s]:
            if dis[e] > s_cost + e_cost:
                dis[e] = s_cost + e_cost
                heappush(q, (dis[e], e))
    return dis

T = int(input())
for tc in range(1, T+1):
    n, m, t = map(int, input().split())
    s, g, h = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    des = []
    answer = []
    for _ in range(m):
        x, y, z = map(int, input().split())
        graph[x].append([y, z])
        graph[y].append([x, z])
    for _ in range(t):
        des.append(int(input()))
    des.sort()
    s_di = di(s)
    g_di = di(g)
    h_di = di(h)
    for d in des:
        if s_di[d] == float('inf'):
            continue
        if s_di[d] == s_di[g] + g_di[h] + h_di[d] or s_di[d] == s_di[h] + h_di[g] + g_di[d]:
            answer.append(d)
    print(*answer)