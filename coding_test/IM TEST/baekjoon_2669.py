# 직사각형 네개의 합집합의 면적 구하기

matrix = [[0]*101 for _ in range(101)]
for _ in range(4):
    tmp = list(map(int, input().split()))
    for i in range(tmp[0], tmp[2]):
        for j in range(tmp[1], tmp[3]):
            matrix[j][i] = 1

cnt = 0
for i in range(101):
    cnt += matrix[i].count(1)
print(cnt)