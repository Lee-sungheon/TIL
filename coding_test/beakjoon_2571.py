# 색종이 - 3
N = int(input())
matrix = [[0]*101 for _ in range(101)]
for _ in range(N):
    x, y = map(int, input().split())
    for i in range(y, y+10):
        for j in range(x, x+10):
            matrix[i][j] += 1
for i in range(101):
    print(matrix[i])