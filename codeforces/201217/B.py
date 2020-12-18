# Find The Array
import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    s = sum(a)
    result = []
    total = 0
    for i in range(1, n):
        if a[i] % a[i-1] == 0 or a[i-1] % a[i] == 0:
            result.append(a[i-1])
            total += 0
        else:
            pass
