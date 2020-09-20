# 색종이

matrix = [[0]*100 for _ in range(100)]
N = int(input())
for _ in range(N):
    x, y = map(int, input().split())
    for i in range(x, x+10):
        for j in range(y, y+10):
            matrix[j][i] = 1
cnt = 0
for i in range(100):
    cnt += matrix[i].count(1)
print(cnt)