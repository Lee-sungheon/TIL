# 그렇고 그런 사이
import sys


input = sys.stdin.readline
n, k = map(int, input().split())
start, end = 1, n
for i in range(1, n+1):
    if n-i <= k:
        print(end, end=' ')
        k -= (n-i)
        end -= 1
    else:
        print(start, end=' ')
        start += 1