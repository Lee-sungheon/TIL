# 정육점 (정렬, 그리디)
import sys

N, M = map(int, sys.stdin.readline().split())
meats = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
meats.sort(key=lambda x: (x[1], -x[0]))
costs = []
for i in range(N):
    costs.append(meats[i][1])
costs = list(set(costs))
costs += [costs[len(costs)-1]]
result = meats[0][0]
cost = meats[0][1]
for i in range(1, N):
    if result >= M:
        cost = min(cost, costs[costs.index(meats[i][1])+1])
        break
    result += meats[i][0]
    if meats[i-1][1] == meats[i][1]:
        cost += meats[i][1]
    else:
        cost = meats[i][1]
if result < M:
    cost = -1
print(cost)