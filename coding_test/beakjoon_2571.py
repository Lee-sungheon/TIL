# 색종이 - 3
N = int(input())
matrix = [[0]*101 for _ in range(101)]
for _ in range(N):
    x, y = map(int, input().split())
    for i in range(y, y+10):
        for j in range(x, x + 10):
            matrix[i][j] += 1
# for i in range(101):
#     print(matrix[i])

col_max = row_max = 0
col_min = row_min = 101
for i in range(101):
    for j in range(101):
        if matrix[i][j] > 1:
            if j > col_max:
                col_max = j
            if i > row_max:
                row_max = i
            if j < col_min:
                col_min = j
            if i < row_min:
                row_min = i
if col_min == 101:
    col_min = 0
if row_min == 101:
    row_min = 0
col_cnt = row_max - row_min
for i in range(row_min-1, -1, -1):
    tmp = 0
    for j in range(col_min, col_max+1):
        if matrix[i][j] >= 1:
            tmp += 1
        else:
            break
    if tmp == col_max - col_min + 1:
        col_cnt += 1
    else:
        break
for i in range(row_max, 101):
    tmp = 0
    for j in range(col_min, col_max+1):
        if matrix[i][j] >= 1:
            tmp += 1
        else:
            break
    if tmp == col_max - col_min + 1:
        col_cnt += 1
    else:
        break
row_cnt = col_max - col_min
for i in range(col_min-1, -1, -1):
    tmp = 0
    for j in range(row_min, row_max+1):
        if matrix[j][i] >= 1:
            tmp += 1
        else:
            break
    if tmp == row_max - row_min + 1:
        row_cnt += 1
    else:
        break
for i in range(col_max, 101):
    tmp = 0
    for j in range(row_min, row_max+1):
        if matrix[j][i] >= 1:
            tmp += 1
        else:
            break
    if tmp == row_max - row_min + 1:
        row_cnt += 1
    else:
        break
col_max, row_max = col_max + 1, row_max + 1
print(col_min, col_max, row_min, row_max)
print(col_cnt * (col_max - col_min))
print(row_cnt * (row_max - row_min))
print(max(col_cnt * (col_max - col_min), row_cnt * (row_max - row_min)))
