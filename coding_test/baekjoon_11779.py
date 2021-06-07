# 최소비용 구하기2 (다익스트라)
import heapq
import sys


def di(idx):
    queue = []
    K_distance = [INF for _ in range(N + 1)]
    K_distance[idx] = 0
    heapq.heappush(queue, [0, idx])
    while queue:
        mid = heapq.heappop(queue)
        if K_distance[mid[1]] < mid[0]:
            continue
        for end in distance[mid[1]]:
            if K_distance[end[0]] > mid[0] + end[1]:
                res[end[0]] = res[mid[1]] + [end[0]]
                K_distance[end[0]] = mid[0] + end[1]
                heapq.heappush(queue, [K_distance[end[0]], end[0]])
    return K_distance


input = sys.stdin.readline
N = int(input())
M = int(input())
distance = [[] for _ in range(N + 1)]
INF = 100000 * M + 1
for _ in range(M):
    x, y, z = map(int, input().split())
    distance[x].append([y, z])
S, E = map(int, input().split())
res = [[S] for _ in range(N+1)]
result = di(S)
print(result[E])
print(len(res[E]))
print(*res[E])
