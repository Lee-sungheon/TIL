# 나이순 정렬
import sys
input = sys.stdin.readline
n = int(input())
array = [input().split() for _ in range(n)]
for arr in array:
    arr[0] = int(arr[0])
array.sort(key=lambda x:(x[0]))
for arr in array:
    print(arr[0], arr[1])
