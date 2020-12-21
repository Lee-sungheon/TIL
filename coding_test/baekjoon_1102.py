# 발전소

n = int(input())
plant = [list(map(int, input().split())) for _ in range(n)]
on_off = list(input())
on_num = int(input())
cost = [0] * n
for i in range(n):
    if on_off[i] == 'N':
        cost[i] = 51

for i in range(n):
    for j in range(n):
        if on_off[j] == 'N' and i != j:
            tmp = plant[i][j]
            if tmp < cost[j]:
                cost[j] = tmp

cost.sort()
cost = cost[:on_num]
if cost.count(51) > 0:
    print(-1)
else:
    print(sum(cost))