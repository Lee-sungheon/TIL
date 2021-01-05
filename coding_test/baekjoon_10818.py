# 최소, 최대값

import sys

n = int(input())
numbers = list(map(int, input().split()))
min_num = sys.maxsize
max_num = -sys.maxsize
for num in numbers:
    if min_num > num:
        min_num = num
    if max_num < num:
        max_num = num

print(min_num, max_num)