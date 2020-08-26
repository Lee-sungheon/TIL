# Ladder1
for tc in range(10):
    T = int(input())
    N = 100
    radder_list = [list(map(int, input().split())) for _ in range(N)]
    x = radder_list[99].index(2)
    i = 99
    while True:
        if x-1 >= 0 and radder_list[i][x-1] == 1:
            radder_list[i][x] = 2
            x -= 1
        elif x+1 <= 99 and radder_list[i][x+1] == 1:
            radder_list[i][x] = 2
            x += 1
        else:
            i -= 1
        if i == 0:
            break
    print(f'#{T} {x}')