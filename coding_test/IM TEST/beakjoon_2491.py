# 수열
import sys
N = int(input())
arr = list(map(int, sys.stdin.readline().split()))
cnt1 = cnt2 = 1
max_cnt = 1
for i in range(1, N):
    if arr[i] >= arr[i-1]:
        cnt1 += 1
    else:
        if cnt1 > max_cnt:
            max_cnt = cnt1
        cnt1 = 1
    if arr[i] <= arr[i-1]:
        cnt2 += 1
    else:
        if cnt2 > max_cnt:
            max_cnt = cnt2
        cnt2 = 1
    if cnt1 > max_cnt:
        max_cnt = cnt1
    if cnt2 > max_cnt:
        max_cnt = cnt2
print(max_cnt)