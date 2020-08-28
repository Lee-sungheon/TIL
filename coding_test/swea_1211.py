# Ladder2
import copy

for tc in range(10):
    T = int(input())
    N = 100
    radder_list = [list(map(int, input().split())) for _ in range(N)]
    x = []
    for i in range(100):
        if radder_list[0][i] == 1:
            x.append([0, i, i])
    for j in range(len(x)):
        i = 1
        radder_list2 = copy.deepcopy(radder_list)
        while i < 99:
            if x[j][1]-1 >= 0 and radder_list2[i][x[j][1]-1] == 1:
                radder_list2[i][x[j][1]] = 2
                x[j][1] -= 1
            elif x[j][1]+1 <= 99 and radder_list2[i][x[j][1]+1] == 1:
                radder_list2[i][x[j][1]] = 2
                x[j][1] += 1
            else:
                i += 1
            x[j][0] += 1

    print(f'#{T} {min(x)[2]}')