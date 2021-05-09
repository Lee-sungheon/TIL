import heapq

# def solution(n, start, endpoint, roads, traps):
#     V, E = n, len(roads)
#     INF = 3000 * V + 1
#     distance = [[] for _ in range(V + 1)]
#     for road in roads:
#         s, e, dist = road[0], road[1], road[2]
#         distance[s].append([e, dist])
#     queue = []
#     K_distance = [INF for _ in range(V + 1)]
#     K_distance[start] = 0
#     heapq.heappush(queue, [0, 1, []])
#     print(distance)
#     while queue:
#         mid = heapq.heappop(queue)
#         if len(mid[2]) > 0:
#             for road in roads:
#                 s, e, dist = road[0], road[1], road[2]
#                 for m in mid[2]:
#                     if m == s or m == e:
#                         s, e = e, s
#                 distance[s].append([e, dist])
#         for end in distance[mid[1]]:
#             if K_distance[end[0]] > mid[0] + end[1]:
#                 K_distance[end[0]] = mid[0] + end[1]
#                 if end[0] in traps:
#                     if end[0] in mid[2]:
#                         del mid[2][mid[2].index(end[0])]
#                     else:
#                         mid[2].append(end[0])
#                 heapq.heappush(queue, [K_distance[end[0]], end[0], mid[2]])
#
#     return K_distance

def solution(n, start, end, roads, traps):
    def dfs(dfs_s, dfs_distance, dfs_trap, result):
        result.append(dfs_s)
        if (dfs_s == end):
            print(result)
            return
        dfs_distance = [[] for _ in range(V + 1)]
        for road in roads:
            s, e, dist = road[0], road[1], road[2]
            for m in dfs_trap:
                if m == s or m == e:
                    s, e = e, s
            dfs_distance[s].append([e, dist])

        for st in dfs_distance[dfs_s]:
            if st[0] in traps:
                if st[0] in dfs_trap:
                    del dfs_trap[dfs_trap.index(st[0])]
                else:
                    dfs_trap.append(st[0])
            dfs(st[0], dfs_distance, dfs_trap, result)

    V, E = n, len(roads)
    distance = [[] for _ in range(V + 1)]
    for road in roads:
        s, e, dist = road[0], road[1], road[2]
        distance[s].append([e, dist])
    dfs(start, [], [], [])

print(solution(3, 1, 3, [[1, 2, 2], [3, 2, 3]], [2]))
print(solution(4, 1, 4, [[1, 2, 1], [3, 2, 1], [2, 4, 1]], [2, 3]))