# 습격받은 도시
import copy

n = int(input())
city = [list(input()) for _ in range(n)]
copy_city = copy.deepcopy(city)
print(city)
for i in range(n):
    for j in range(n):
        if city[i][j] == 'O':
            pass