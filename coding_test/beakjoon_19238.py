# 스타트 택시
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
        if f <= 0:
            return end
        elif matrix[x][y] > 1:
            end.append(([x, y], cnt))
        for dx, dy in delta:
            nx, ny = x + dx, y + dy
            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue
            if matrix[nx][ny] != 1 and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                dq.append(([nx, ny], cnt+1, f-1))


def bfs2(start, fuel, man_number):
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
        if matrix[x][y] == -man_number:
            end.append(([x, y], cnt))
            return end
        for sam in same:
            same_tmp = sam
            if x == same_tmp[0][0] and y == same_tmp[0][1] and same_tmp[1] == -man_number:
                end.append(([same_tmp[0][0], same_tmp[0][1]], cnt))
                return end
        if f <= 0:
            return end
        for dx, dy in delta:
            nx, ny = x + dx, y + dy
            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue
            if matrix[nx][ny] != 1 and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                dq.append(([nx, ny], cnt+1, f-1))


N, M, fuel = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
start = list(map(int, input().split()))
start[0], start[1] = start[0] - 1, start[1] - 1
same = []
for i in range(M):
    tmp = list(map(int, input().split()))
    matrix[tmp[0]-1][tmp[1]-1] = i + 2
    if matrix[tmp[2]-1][tmp[3]-1] != 0:
        same.append(((tmp[0]-1, tmp[1]-1), -(i + 2)))
    else:
        matrix[tmp[2]-1][tmp[3]-1] = - (i + 2)
man_number = 0
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
    man_number = matrix[start[0]][start[1]]
    matrix[start[0]][start[1]] = 0

    temp = bfs2(start, fuel, man_number)
    if not temp:
        print(-1)
        break
    result = temp[0]
    fuel -= result[1]
    start = result[0]
    fuel = fuel + 2*result[1]
else:
    print(fuel)
