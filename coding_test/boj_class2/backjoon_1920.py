# 종말의 수
import sys
input = sys.stdin.readline
N = int(input())
nums = set(input().split())
M = int(input())
for num in input().split():
    if num in nums:
        print(1)
    else:
        print(0)
