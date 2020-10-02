# 색종이 - 3
def find_index(i, j):
    col_min.append(j)
    row_min.append(i)
    for m in range(i, 101):
        if matrix[m][j] > 1 and (m == 100 or matrix[m+1][j] <= 1):
            row_max.append(m)
            break
    for n in range(j, 101):
        if matrix[i][n] > 1 and (n == 100 or matrix[i][n+1] <= 1):
            col_max.append(n)
            break

    for i in range(row_min[-1], row_max[-1] + 1):
        for j in range(col_min[-1], col_max[-1] + 1):
            matrix[i][j] = 110
    return


N = int(input())
matrix = [[0]*101 for _ in range(101)]
for _ in range(N):
    x, y = map(int, input().split())
    for i in range(y, y+10):
        for j in range(x, x + 10):
            matrix[i][j] += 1

col_max, row_max = [], []
col_min, row_min = [], []
for i in range(101):
    for j in range(101):
        if 101 > matrix[i][j] > 1:
            find_index(i, j)

max_result = 0
for k in range(len(row_min)):
    if col_min[k] == 101:
        col_min[k] = 0
    if row_min[k] == 101:
        row_min[k] = 0
    col_cnt = row_max[k] - row_min[k]
    for i in range(row_min[k] - 1, -1, -1):
        tmp = 0
        for j in range(col_min[k], col_max[k] + 1):
            if matrix[i][j] >= 1:
                tmp += 1
            else:
                break
        if tmp == col_max[k] - col_min[k] + 1:
            col_cnt += 1
        else:
            break
    for i in range(row_max[k], 101):
        tmp = 0
        for j in range(col_min[k], col_max[k] + 1):
            if matrix[i][j] >= 1:
                tmp += 1
            else:
                break
        if tmp == col_max[k] - col_min[k] + 1:
            col_cnt += 1
        else:
            break

    row_cnt = col_max[k] - col_min[k]
    for i in range(col_min[k] - 1, -1, -1):
        tmp = 0
        for j in range(row_min[k], row_max[k] + 1):
            if matrix[j][i] >= 1:
                tmp += 1
            else:
                break
        if tmp == row_max[k] - row_min[k] + 1:
            row_cnt += 1
        else:
            break
    for i in range(col_max[k], 101):
        tmp = 0
        for j in range(row_min[k], row_max[k] + 1):
            if matrix[j][i] >= 1:
                tmp += 1
            else:
                break
        if tmp == row_max[k] - row_min[k] + 1:
            row_cnt += 1
        else:
            break
    col_max[k], row_max[k] = col_max[k] + 1, row_max[k] + 1
    max_result = max(max_result, col_cnt * (col_max[k] - col_min[k]), row_cnt * (row_max[k] - row_min[k]))
print(max_result)