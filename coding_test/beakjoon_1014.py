# T = int(input())
# for tc in range(T):
#     N, M = map(int, input().split())
#     room = [list(input()) for _ in range(N)]
#     rooms = [[0]*N for _ in range(M)]
#     seat = []
#     for i in range(M):
#         for j in range(N):
#             rooms[i][j] = room[j][i]
    
#     for i in range(M):
#         seat.append(rooms[i].count('.'))
    
#     total = 0
#     ten = [[0,2,4,6,8],[0,2,4,6,9],[0,2,4,7,9],[0,2,5,7,9],[0,3,5,7,9],[1,3,5,7,9]]
#     eight = [[0,2,4,6],[0,2,4,7],[0,2,5,7],[0,3,5,7],[1,3,5,7]]
#     six = [[0,2,4],[0,2,5],[0,3,5],[1,3,5]]
#     four = [[0,2],[0,3],[1,3]]
#     two = [[0],[1]]

#     if M % 2:
#         print(max(sum(seat[::2]), sum(seat[1::2])))
#     else:
#         max_total = 0
#         if M == 10:
#             for i in range(len(ten)):
#                 total = 0
#                 for j in range(len(ten[0])):
#                     total += seat[ten[i][j]]
#                 if max_total < total:
#                     max_total = total
#         elif M == 8:
#             for i in range(len(eight)):
#                 total = 0
#                 for j in range(len(eight[0])):
#                     total += seat[eight[i][j]]
#                 if max_total < total:
#                     max_total = total
#         elif M == 6:
#             for i in range(len(six)):
#                 total = 0
#                 for j in range(len(six[0])):
#                     total += seat[six[i][j]]
#                 if max_total < total:
#                     max_total = total
#         elif M == 4:
#             for i in range(len(four)):
#                 total = 0
#                 for j in range(len(four[0])):
#                     total += seat[four[i][j]]
#                 if max_total < total:
#                     max_total = total
#         elif M == 2:
#             for i in range(len(two)):
#                 total = 0
#                 for j in range(len(two[0])):
#                     total += seat[two[i][j]]
#                 if max_total < total:
#                     max_total = total
#         print(max_total)



import sys
import re
T = int(sys.stdin.readline())
results = []

def dfs(x):
    global bimap
    global matched
    global visited
    if visited[x]: return False
    visited[x] = True
    for y, link in enumerate(bimap[x]):
        if link:
            # bimap[x][y] = 0 # visited
            if y not in matched or dfs(matched[y]):
                matched[y] = x
                return True
    return False

for _ in range(T):
    M, N = map(int, sys.stdin.readline().split())
    x_start = 0
    x_idx = 0
    y_start = 0
    y_idx = 0
    max = 0
    matched = {}
    sit_cnt = 0

    # 교실 모든 자리를 0으로 초기화
    coord_map = []
    for _ in range(M):
        coord_map.append([0 for _ in range(N)])

    X = {}
    Y = {}
    
    bimap = []
    if N % 2 == 0:
        for _ in range(int(N/2)*M): bimap.append([0 for _ in range(int(N/2)*M)])
    else:
        for _ in range((int(N/2)+1)*M): bimap.append([0 for _ in range(int(N/2)*M)])

    # 입력받은 교실 의자의 정보를 이분 매칭(좌측 열을 X, 우측 열을 Y로 표현)의 형태로 분리함.
    # X는 홀수열, Y는 짝수열로 둠. 각 열 내에서는 컨닝이 불가하므로
    # 홀수열과 짝수열을 각각 이어 붙이면 이분 그래프를 그릴 수 있음.
    # X, Y 모두 딕셔너리 이고, {(X 좌표, Y 좌표): (이분 매칭에서의 번호, 의자가 있는지 여부)} 형태로 만듦.
    for x in range(M):
        row = sys.stdin.readline().replace("\n", "")

        turn = "X"
        x_idx = x_start
        y_idx = y_start
        for y, value in enumerate(row):
            if turn == "X":
                if value == ".":
                    X[(x, y)] = (x_idx, 1)
                    sit_cnt += 1
                else: X[(x, y)] = (x_idx, 0)
                x_idx += M
                turn = "Y"
            else:
                if value == ".":
                    Y[(x, y)] = (y_idx, 1)
                    sit_cnt += 1
                else: Y[(x, y)] = (y_idx, 0)
                y_idx += M
                turn = "X"
        x_start += 1
        y_start += 1

        # 각 좌표에 의자가 있는지 확인해 주는 맵 추가
        for y, value in enumerate(row):
            if value == ".": coord_map[x][y] = 1

    # 홀수열(X)에 대해서만 루프를 돌림
    for x, y in X:
        item = X[(x, y)]
        if not item[1]: continue
        # 컨닝이 가능한 위치들
        candidates = [(x-1, y-1), (x, y-1), (x+1, y-1), (x-1, y+1), (x, y+1), (x+1, y+1)]
        for cx, cy in candidates:
            # 컨닝이 가능한 위치들 중에서 의자가 있는 경우, 
            if 0 <= cx < M and 0 <= cy < N and coord_map[cx][cy]:
                # 루프로 돌고 있는 좌표의 이분 그래프 X index와
                # 컨닝이 가능한 자리들의 이분 그래프 Y index를 반환하고
                bigraph_x = X[(x, y)][0]
                bigraph_y = Y[(cx, cy)][0]

                # 그 두 좌표를 이음.
                bimap[bigraph_x][bigraph_y] = 1

    # 이분 그래프에서의 최소 버텍스 커버를 구하기 위한 dfs를 돌림.
    for i in range(len(X)):
        visited = [False for _ in range(len(X))]
        dfs(i)
    
    result = sit_cnt - len(matched)
    results.append(result)

for result in results:
    sys.stdout.write(str(result)+'\n')