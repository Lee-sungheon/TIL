# 음식배달
def search(r, c, cost):
    tmp = []
    for l in range(N):
        for m in range(N):
            if array[l][m] == 1:
                tmp.append((cost+abs(r-l)+abs(c-m), cost))
    total.append(tmp)


T = int(input())
for tc in range(T):
    N = int(input())
    array = [list(map(int, input().split())) for _ in range(N)]
    food = set()
    total = []
    result = 0

    for i in range(N):
        for j in range(N):
            if array[i][j] > 1:
                search(i, j, array[i][j])
    print(total)

    for i in range(len(total[0])):
        min_num = [1000000000, 0]
        for j in range(len(total)):
            if total[j][i][0] < min_num[0]:
                min_num[0] = total[j][i][0]
                min_num[1] = total[j][i][1]
        print(min_num)
        result += min_num[0] - min_num[1]
        food.add(min_num[1])
    result += sum(food)
    print(food)
    print(result)
