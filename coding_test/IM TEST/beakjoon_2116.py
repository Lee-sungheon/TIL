# 주사위 쌓기
import sys

N = int(sys.stdin.readline())
dice_li = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
sum_li = []
couple = {0: 5, 1: 3, 2: 4, 5: 0, 3: 1, 4: 2}
for i in range(6):
    total = 0
    idx = i
    x_li = [[dice_li[0][idx], dice_li[0][couple[idx]]]]
    idx = couple[idx]
    for j in range(1, N):
        idx = dice_li[j].index(dice_li[j-1][idx])
        x_li.append([dice_li[j][idx], dice_li[j][couple[idx]]])
        idx = couple[idx]

    total = 0
    for j in range(N):
        if 6 not in x_li[j]:
            total += 6
        elif 5 not in x_li[j]:
            total += 5
        else:
            total += 4
    sum_li.append(total)
print(max(sum_li))