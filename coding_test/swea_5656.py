# [모의 SW 역량테스트] 벽돌 깨기
import copy


def dfs(cnt, mat):
    global result
    if cnt == N:
        total = 0
        for i in range(H):
            total += (W - mat[i].count(0))
        if total < result:
            result = total
        return

    if result == 0:
        return

    for i in range(W):
        is_shoot = False
        for j in range(H):
            if mat[j][i] != 0:
                tmp_matrix = copy.deepcopy(mat)
                value = tmp_matrix[j][i]
                tmp_matrix[j][i] = 0
                shoot(i, j, value, tmp_matrix)
                tmp_matrix = sort(tmp_matrix)
                is_shoot = True
                break
        if is_shoot:
            dfs(cnt+1, tmp_matrix)
    else:
        total = 0
        for i in range(H):
            total += (W - mat[i].count(0))
        if total < result:
            result = total


def shoot(x, y, value, tmp_matrix):
    delta = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    for i in range(value):
        for dx, dy in delta:
            nx = x + (dx*i)
            ny = y + (dy*i)
            if nx < 0 or ny < 0 or nx >= W or ny >= H:
                continue
            if tmp_matrix[ny][nx] == 0:
                continue
            else:
                value = tmp_matrix[ny][nx]
                tmp_matrix[ny][nx] = 0
                shoot(nx, ny, value, tmp_matrix)


def sort(mat):
    tmp = [[0]*W for _ in range(H)]
    for j in range(W):
        idx = H-1
        for i in range(H-1, -1, -1):
            if mat[i][j] != 0:
                tmp[idx][j] = mat[i][j]
                idx -= 1
    return tmp


T = int(input())
for tc in range(T):
    N, W, H = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(H)]
    result = 180
    dfs(0, matrix)
    print("#{} {}" .format(tc+1, result))