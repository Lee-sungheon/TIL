# 구간 합 구하기4
import sys
def solution():
    N, M = map(int, sys.stdin.readline().split())
    sum_li = [0] + list(map(int, sys.stdin.readline().split()))
    for i in range(1, N):
        sum_li[i] = sum_li[i] + sum_li[i-1]
    for _ in range(M):
        i, j = map(int, sys.stdin.readline().split())
        print(sum_li[j] - sum_li[i-1])


solution()