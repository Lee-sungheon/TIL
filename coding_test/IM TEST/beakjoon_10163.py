# 색종이

N = int(input())
matrix = [[0]*101 for _ in range(101)]
cnt = [0]*(N+1)
for i in range(1, N+1):
    tmp = list(map(int, input().split()))
    for j in range(0, tmp[2]):
        for k in range(0, tmp[3]):
            matrix[tmp[0]+j][tmp[1]+k] = i

for i in range(101):
    for j in range(101):
        if matrix[i][j] > 0:
            cnt[matrix[i][j]] += 1
cnt.pop(0)
print(*cnt, sep='\n')
