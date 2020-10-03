# 색종이 - 3
def find_area(col_min, row_min):
    max_result = 0
    row_max = col_max = 0
    is_true = False
    for m in range(col_min, 101):
        if matrix[m][row_min] == 1 and (m == 100 or matrix[m+1][row_min] == 0):
            col_max = m
            for i in range(row_min, 101):
                for j in range(col_min, col_max+1):
                    if matrix[j][i] == 0:
                        row_max = j
                        is_true = True
                        break
                if is_true:
                    is_true = False
                    break
            break
    max_result = max(max_result, ((row_max+1)-row_min)*((col_max+1)-col_min))
    # print(row_min, row_max, col_min, col_max)
    for n in range(row_min, 101):
        if matrix[col_min][n] == 1 and (n == 100 or matrix[col_min][n+1] == 0):
            row_max = n
            for i in range(col_min, 101):
                for j in range(row_min, row_max + 1):
                    if matrix[i][j] == 0:
                        col_max = i
                        is_true = True
                        break
                if is_true:
                    is_true = False
                    break
            break
    max_result = max(max_result, ((row_max+1) - row_min)*((col_max) - col_min))
    # print(row_min, row_max, col_min, col_max)
    return max_result



N = int(input())
matrix = [[0]*101 for _ in range(101)]
for _ in range(N):
    x, y = map(int, input().split())
    for i in range(y, y + 10):
        for j in range(x, x + 10):
            matrix[i][j] = 1

max_result = 0
for i in range(101):
    for j in range(101):
        if matrix[i][j] == 1:
            max_result = max(max_result, find_area(i, j))

print(max_result)