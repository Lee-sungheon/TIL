# 무엇을 아느냐가 아니라 누구를 아느냐가 문제다 (다익스트라)

import heapq
import sys

input = sys.stdin.readline

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    graph = [[] for _ in range(M)]
    res = [[0] for _ in range(M)]
    INF = 4 * N + 1
    for _ in range(N):
        x, y, z = map(int, input().split())
        graph[x].append([y, z])
        graph[y].append([x, z])
    print(graph)

    # 다익스트라
    queue = []
    distance = [INF for _ in range(M)]
    distance[0] = 0
    heapq.heappush(queue, [0, 0])
    while queue:
        s_cost, s = heapq.heappop(queue)
        print(queue)
        # 가지치기
        if distance[s] < s_cost:
            continue
        # 다익스트라 본격 시작
        for e, e_cost in graph[s]:
            if distance[e] > s_cost + e_cost:
                res[e] = res[s] + [e]
                distance[e] = s_cost + e_cost
                heapq.heappush(queue, [distance[e], e])
    if distance[M-1] == INF:
        print("Case #{}: -1" .format(tc))
    else:
        print(f"Case #{tc}: ", end="")
        print(*res[-1])
    print(res)
