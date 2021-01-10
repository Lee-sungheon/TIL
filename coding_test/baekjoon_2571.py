# 색종이 - 3
def isPaper(r, c, w, h):
    for i in range(r, r+h+1):
        for j in range(c, c+w+1):
            if matrix[i][j] != 1:
                return 0
    return 1


def find_area(r, c):
    global max_result
    for w in range(101):
        if c+w > 101 or matrix[r][c+w] == 0:
            break
        for h in range(101):
            if r+h > 101 or matrix[r+h][c] == 0:
                break
            if isPaper(r, c, w, h):
                max_result = max(max_result, (w+1)*(h+1))


N = int(input())
matrix = [[0]*101 for _ in range(101)]
for _ in range(N):
    x, y = map(int, input().split())
    for i in range(y, y + 10):
        for j in range(x, x + 10):
            matrix[i][j] = 1
max_result = 0
for r in range(101):
    for c in range(101):
        if matrix[r][c] == 1:
            find_area(r, c)
print(max_result)