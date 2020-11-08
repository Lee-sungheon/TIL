# 최소 이동 거리
import heapq

T = int(input())
for tc in range(T):
    V, E = map(int, input().split())
    INF = 10 * V + 1
    distance = [[] for _ in range(V + 1)]
    for _ in range(E):
        start, end, dist = map(int, input().split())
        distance[start].append([end, dist])
    queue = []
    K_distance = [INF for _ in range(V + 1)]
    K_distance[0] = 0
    heapq.heappush(queue, [0, 0])
    while queue:
        mid = heapq.heappop(queue)
        for end in distance[mid[1]]:
            if K_distance[end[0]] > mid[0] + end[1]:
                K_distance[end[0]] = mid[0] + end[1]
                heapq.heappush(queue, [K_distance[end[0]], end[0]])
    print('#{} {}' .format(tc+1, K_distance[-1]))

