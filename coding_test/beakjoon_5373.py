# 큐빙

T = int(input())
for tc in range(T):
    N = int(input())
    rotation = input().split()
    # 상, 하, 앞, 뒤, 좌, 우
    cube = [[['w']*3 for _ in range(3)],[['y']*3 for _ in range(3)],
            [['r']*3 for _ in range(3)],[['o']*3 for _ in range(3)],
            [['g']*3 for _ in range(3)],[['b']*3 for _ in range(3)]]
    print(cube)
    for i in range(N):
        if rotation[i] == 'L-':
            tmp1 = cube[0][0][0]
            tmp2 = cube[0][1][0]
            tmp3 = cube[0][2][0]
            cube[0][0][0] = cube[2][0][0]
            cube[0][1][0] = cube[2][1][0]
            cube[0][2][0] = cube[2][2][0]
            cube[2][0][0] = cube[1][0][0]
            cube[2][1][0] = cube[1][1][0]
            cube[2][2][0] = cube[1][2][0]
            cube[1][0][0] = cube[3][0][0]
            cube[1][1][0] = cube[3][1][0]
            cube[1][2][0] = cube[3][2][0]
            cube[3][0][0] = tmp1
            cube[3][1][0] = tmp2
            cube[3][2][0] = tmp3
        elif rotation[i] == 'L+':
            tmp1 = cube[0][0][0]
            tmp2 = cube[0][1][0]
            tmp3 = cube[0][2][0]
            cube[0][0][0] = cube[2][0][0]
            cube[0][1][0] = cube[2][1][0]
            cube[0][2][0] = cube[2][2][0]
            cube[2][0][0] = cube[1][0][0]
            cube[2][1][0] = cube[1][1][0]
            cube[2][2][0] = cube[1][2][0]
            cube[1][0][0] = cube[3][0][0]
            cube[1][1][0] = cube[3][1][0]
            cube[1][2][0] = cube[3][2][0]
            cube[3][0][0] = tmp1
            cube[3][1][0] = tmp2
            cube[3][2][0] = tmp3

    print(*cube[0])