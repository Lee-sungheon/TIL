# 발전소 (bfs)
import sys
sys.setrecursionlimit(10**6)

def solve(total):
    global result
    if total > result:
        return
    if on_off.count('Y') >= on_num:
        result = min(result, total)
        return
    for i in range(n):
        for j in range(n):
            if on_off[j] == 'N' and i != j:
                tmp = plant[i][j]
                on_off[j] = 'Y'
                solve(total+tmp)
                on_off[j] = 'N'


n = int(input())
result = 5000
plant = [list(map(int, input().split())) for _ in range(n)]
on_off = list(input())
on_num = int(input())

solve(0)

if result == 5000:
    print(-1)
else:
    print(result)