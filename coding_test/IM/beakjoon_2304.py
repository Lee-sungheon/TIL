# 창고 다각형
import sys

N = int(sys.stdin.readline())
array = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]
array.sort()
max_num = 0
total = 0
for i in range(N):
    if max_num < array[i][1]:
        max_num = array[i][1]
max_height = array[0][1]
idx = 0
tmp = 0
for i in range(array[0][0], array[-1][0]+1):
    if i == array[idx][0]:
        if max_height < array[idx][1]:
            max_height = array[idx][1]
        idx += 1
    total += max_height
    if max_height == max_num:
        tmp = i
        break
idx = len(array) - 1
max_height = array[-1][1]
for i in range(array[-1][0], tmp, -1):
    if i == array[idx][0]:
        if max_height < array[idx][1]:
            max_height = array[idx][1]
        idx -= 1
    total += max_height
print(total)