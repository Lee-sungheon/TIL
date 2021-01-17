# 딱지놀이
import sys
N = int(input())
for _ in range(N):
    tmp = list(map(int, sys.stdin.readline().split()))
    A = [tmp[i+1] for i in range(tmp[0])]
    tmp = list(map(int, sys.stdin.readline().split()))
    B = [tmp[i + 1] for i in range(tmp[0])]
    result = []
    for i in range(4, 0, -1):
        result.append((A.count(i), B.count(i)))
    for i in range(4):
        if result[i][0] > result[i][1]:
            print("A")
            break
        elif result[i][0] < result[i][1]:
            print("B")
            break
    else:
        print("D")