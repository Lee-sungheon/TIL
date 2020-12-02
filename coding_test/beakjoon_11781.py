# 퇴근 시간
import heapq, sys


N, M, S, E = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(M)]
INF = sys.maxsize
distance = [[] for _ in range(N + 1)]
for i in range(M):
    start, end, dist, t1, t2 = matrix[i]
    if start > end:
        start, end = end, start
        t1, t2 = t2, t1
    distance[start].append([end, dist, t1, t2])
    distance[end].append([start, dist, t2, t1])
queue = []
K_distance = [INF for _ in range(N + 1)]
K_distance[0] = K_distance[1] = 0
heapq.heappush(queue, [0, 1])
print(distance)
while queue:
    mid = heapq.heappop(queue)
    for end in distance[mid[1]]:
        if E > mid[0] + end[1] >= S:
            pass
        elif mid[0] < S and mid[0] + end[1] > E:
            pass

        tmp = mid[0] + end[1]
        if K_distance[end[0]] > tmp:
            K_distance[end[0]] = tmp
            heapq.heappush(queue, [K_distance[end[0]], end[0]])
print(K_distance)
print(max(K_distance))