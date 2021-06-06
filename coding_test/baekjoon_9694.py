# 무엇을 아느냐가 아니라 누구를 아느냐가 문제다 (다익스트라)

import heapq
import sys

input = sys.stdin.readline

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    distance = [[] for _ in range(M)]
    res = [[0] for _ in range(M)]
    INF = 4 * N + 1
    for _ in range(N):
        x, y, z = map(int, input().split())
        distance[x].append([y, z])
        distance[y].append([x, z])
    queue = []
    K_distance = [INF for _ in range(M)]
    K_distance[0] = 0
    heapq.heappush(queue, [0, 0])
    while queue:
        mid = heapq.heappop(queue)
        if K_distance[mid[1]] < mid[0]:
            continue
        for end in distance[mid[1]]:
            if K_distance[end[0]] > mid[0] + end[1]:
                res[end[0]] = res[mid[1]] + [end[0]]
                K_distance[end[0]] = mid[0] + end[1]
                heapq.heappush(queue, [K_distance[end[0]], end[0]])
    if K_distance[M-1] == INF:
        print("Case #{}: -1" .format(tc))
    else:
        print(f"Case #{tc}: ", end="")
        print(*res[-1])
