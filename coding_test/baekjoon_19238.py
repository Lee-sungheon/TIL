# 스타트 택시
import copy
import sys

input = sys.stdin.readline

def bfs(start, fuel):
    dq = [(start, 0, fuel)]
    delta = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    visited = [[0]*N for _ in range(N)]
    visited[start[0]][start[1]] = 1
    end = []
    while dq:
        tmp = list(dq.pop(0))
        x, y = tmp[0]
        cnt = tmp[1]
        f = tmp[2]
        if len(end) != 0 and cnt == end[-1][1]+1:
            return end
        if matrix[x][y] > 1:
            end.append(([x, y], cnt))
        if f < 0:
            return end
        for dx, dy in delta:
            nx, ny = x + dx, y + dy
            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue
            if matrix[nx][ny] != 1 and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                dq.append(([nx, ny], cnt+1, f-1))
    if len(end) != 0:
        return end


def bfs2(start, fuel):
    dq = [(start, 0, fuel)]
    delta = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    visited = [[0]*N for _ in range(N)]
    visited[start[0]][start[1]] = 1
    end = []
    while dq:
        tmp = list(dq.pop(0))
        x, y = tmp[0]
        cnt = tmp[1]
        f = tmp[2]
        if f < 0:
            return end
        if matrix2[x][y] == -1:
            end.append(([x, y], cnt))
            matrix2[x][y] = 0
            return end
        for dx, dy in delta:
            nx, ny = x + dx, y + dy
            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue
            if matrix2[nx][ny] != 1 and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                dq.append(([nx, ny], cnt+1, f-1))
    if len(end) != 0:
        return end


N, M, fuel = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
matrix2 = copy.deepcopy(matrix)
start = list(map(int, input().split()))
start[0], start[1] = start[0] - 1, start[1] - 1
des = []
for i in range(M):
    tmp = list(map(int, input().split()))
    matrix[tmp[0]-1][tmp[1]-1] = i + 2
    des.append(((tmp[2]-1, tmp[3]-1), (i + 2)))
for i in range(M):
    temp = bfs(start, fuel)
    if not temp:
        print(-1)
        break
    elif len(temp) > 1:
        temp.sort()
    result = temp[0]
    fuel -= result[1]
    start = result[0]
    for d in des:
        if d[1] == matrix[start[0]][start[1]]:
            matrix2[d[0][0]][d[0][1]] = -1
    matrix[start[0]][start[1]] = 0
    temp = bfs2(start, fuel)
    if not temp:
        print(-1)
        break
    result = temp[0]
    fuel -= result[1]
    start = result[0]
    fuel = fuel + 2*result[1]
else:
    print(fuel)