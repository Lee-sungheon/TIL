# 큐빙 (구현, 시뮬)
import sys


def rotate(idx, d):
    ret = [[0] * 3 for _ in range(3)]
    if d == 0:
        for r in range(3):
            for c in range(3):
                ret[c][2-r] = cube[idx][r][c]
    elif d == 1:
        for r in range(3):
            for c in range(3):
                ret[2-c][r] = cube[idx][r][c]
    return ret


T = int(input())
for tc in range(T):
    N = int(sys.stdin.readline())
    rotation = sys.stdin.readline().split()
    cube = [[['w']*3 for _ in range(3)],[['y']*3 for _ in range(3)],
            [['r']*3 for _ in range(3)],[['o']*3 for _ in range(3)],
            [['g']*3 for _ in range(3)],[['b']*3 for _ in range(3)]]
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
            cube[1][0][0] = cube[3][2][2]
            cube[1][1][0] = cube[3][1][2]
            cube[1][2][0] = cube[3][0][2]
            cube[3][2][2] = tmp1
            cube[3][1][2] = tmp2
            cube[3][0][2] = tmp3
            cube[4] = rotate(4, 1)
        elif rotation[i] == 'L+':
            tmp1 = cube[0][0][0]
            tmp2 = cube[0][1][0]
            tmp3 = cube[0][2][0]
            cube[0][0][0] = cube[3][2][2]
            cube[0][1][0] = cube[3][1][2]
            cube[0][2][0] = cube[3][0][2]
            cube[3][2][2] = cube[1][0][0]
            cube[3][1][2] = cube[1][1][0]
            cube[3][0][2] = cube[1][2][0]
            cube[1][0][0] = cube[2][0][0]
            cube[1][1][0] = cube[2][1][0]
            cube[1][2][0] = cube[2][2][0]
            cube[2][0][0] = tmp1
            cube[2][1][0] = tmp2
            cube[2][2][0] = tmp3
            cube[4] = rotate(4, 0)
        elif rotation[i] == 'R+':
            tmp1 = cube[0][0][2]
            tmp2 = cube[0][1][2]
            tmp3 = cube[0][2][2]
            cube[0][0][2] = cube[2][0][2]
            cube[0][1][2] = cube[2][1][2]
            cube[0][2][2] = cube[2][2][2]
            cube[2][0][2] = cube[1][0][2]
            cube[2][1][2] = cube[1][1][2]
            cube[2][2][2] = cube[1][2][2]
            cube[1][0][2] = cube[3][2][0]
            cube[1][1][2] = cube[3][1][0]
            cube[1][2][2] = cube[3][0][0]
            cube[3][2][0] = tmp1
            cube[3][1][0] = tmp2
            cube[3][0][0] = tmp3
            cube[5] = rotate(5, 0)
        elif rotation[i] == 'R-':
            tmp1 = cube[0][0][2]
            tmp2 = cube[0][1][2]
            tmp3 = cube[0][2][2]
            cube[0][0][2] = cube[3][2][0]
            cube[0][1][2] = cube[3][1][0]
            cube[0][2][2] = cube[3][0][0]
            cube[3][2][0] = cube[1][0][2]
            cube[3][1][0] = cube[1][1][2]
            cube[3][0][0] = cube[1][2][2]
            cube[1][0][2] = cube[2][0][2]
            cube[1][1][2] = cube[2][1][2]
            cube[1][2][2] = cube[2][2][2]
            cube[2][0][2] = tmp1
            cube[2][1][2] = tmp2
            cube[2][2][2] = tmp3
            cube[5] = rotate(5, 1)
        elif rotation[i] == 'U-':
            tmp = cube[2][0]
            cube[2][0] = cube[4][0]
            cube[4][0] = cube[3][0]
            cube[3][0] = cube[5][0]
            cube[5][0] = tmp
            cube[0] = rotate(0, 1)
        elif rotation[i] == 'U+':
            tmp = cube[2][0]
            cube[2][0] = cube[5][0]
            cube[5][0] = cube[3][0]
            cube[3][0] = cube[4][0]
            cube[4][0] = tmp
            cube[0] = rotate(0, 0)
        elif rotation[i] == 'D+':
            tmp = cube[2][2]
            cube[2][2] = cube[4][2]
            cube[4][2] = cube[3][2]
            cube[3][2] = cube[5][2]
            cube[5][2] = tmp
            cube[1] = rotate(1, 0)
        elif rotation[i] == 'D-':
            tmp = cube[2][2]
            cube[2][2] = cube[5][2]
            cube[5][2] = cube[3][2]
            cube[3][2] = cube[4][2]
            cube[4][2] = tmp
            cube[1] = rotate(1, 1)
        elif rotation[i] == 'F-':
            tmp1, tmp2, tmp3 = cube[0][2][0], cube[0][2][1], cube[0][2][2]
            cube[0][2][0] = cube[5][0][0]
            cube[0][2][1] = cube[5][1][0]
            cube[0][2][2] = cube[5][2][0]
            cube[5][0][0] = cube[1][0][2]
            cube[5][1][0] = cube[1][0][1]
            cube[5][2][0] = cube[1][0][0]
            cube[1][0][2] = cube[4][2][2]
            cube[1][0][1] = cube[4][1][2]
            cube[1][0][0] = cube[4][0][2]
            cube[4][0][2] = tmp3
            cube[4][1][2] = tmp2
            cube[4][2][2] = tmp1
            cube[2] = rotate(2, 1)
        elif rotation[i] == 'F+':
            tmp1, tmp2, tmp3 = cube[0][2][0], cube[0][2][1], cube[0][2][2]
            cube[0][2][0] = cube[4][2][2]
            cube[0][2][1] = cube[4][1][2]
            cube[0][2][2] = cube[4][0][2]
            cube[4][2][2] = cube[1][0][2]
            cube[4][1][2] = cube[1][0][1]
            cube[4][0][2] = cube[1][0][0]
            cube[1][0][2] = cube[5][0][0]
            cube[1][0][1] = cube[5][1][0]
            cube[1][0][0] = cube[5][2][0]
            cube[5][0][0] = tmp1
            cube[5][1][0] = tmp2
            cube[5][2][0] = tmp3
            cube[2] = rotate(2, 0)
        elif rotation[i] == 'B-':
            tmp1, tmp2, tmp3 = cube[0][0][0], cube[0][0][1], cube[0][0][2]
            cube[0][0][0] = cube[4][2][0]
            cube[0][0][1] = cube[4][1][0]
            cube[0][0][2] = cube[4][0][0]
            cube[4][2][0] = cube[1][2][2]
            cube[4][1][0] = cube[1][2][1]
            cube[4][0][0] = cube[1][2][0]
            cube[1][2][2] = cube[5][0][2]
            cube[1][2][1] = cube[5][1][2]
            cube[1][2][0] = cube[5][2][2]
            cube[5][0][2] = tmp1
            cube[5][1][2] = tmp2
            cube[5][2][2] = tmp3
            cube[3] = rotate(3, 1)
        elif rotation[i] == 'B+':
            tmp1, tmp2, tmp3 = cube[0][0][0], cube[0][0][1], cube[0][0][2]
            cube[0][0][0] = cube[5][0][2]
            cube[0][0][1] = cube[5][1][2]
            cube[0][0][2] = cube[5][2][2]
            cube[5][0][2] = cube[1][2][2]
            cube[5][1][2] = cube[1][2][1]
            cube[5][2][2] = cube[1][2][0]
            cube[1][2][2] = cube[4][2][0]
            cube[1][2][1] = cube[4][1][0]
            cube[1][2][0] = cube[4][0][0]
            cube[4][0][0] = tmp3
            cube[4][1][0] = tmp2
            cube[4][2][0] = tmp1
            cube[3] = rotate(3, 0)
        for i in range(6):
            print(cube[i])
        print()
    for i in range(3):
        print(''.join(cube[0][i]))



# def rotate(idx):
#     ret = [[0] * 3 for _ in range(3)]
#     for r in range(3):
#         for c in range(3):
#             ret[c][2-r] = cube[idx][r][c]
#     return ret
#
#
# T = int(input())
# for tc in range(T):
#     N = int(input())
#     rotation = input().split()
#     # 상, 하, 앞, 뒤, 좌, 우
#     cube = [[['w']*3 for _ in range(3)],[['y']*3 for _ in range(3)],
#             [['r']*3 for _ in range(3)],[['o']*3 for _ in range(3)],
#             [['g']*3 for _ in range(3)],[['b']*3 for _ in range(3)]]
#     for i in range(N):
#         if rotation[i][1] == '+':
#             a = 1
#         else:
#             a = 3
#         if rotation[i][0] == 'L':
#             for _ in range(a):
#                 tmp1 = cube[0][0][0]
#                 tmp2 = cube[0][1][0]
#                 tmp3 = cube[0][2][0]
#                 cube[0][0][0] = cube[3][2][2]
#                 cube[0][1][0] = cube[3][1][2]
#                 cube[0][2][0] = cube[3][0][2]
#                 cube[3][2][2] = cube[1][0][0]
#                 cube[3][1][2] = cube[1][1][0]
#                 cube[3][0][2] = cube[1][2][0]
#                 cube[1][0][0] = cube[2][0][0]
#                 cube[1][1][0] = cube[2][1][0]
#                 cube[1][2][0] = cube[2][2][0]
#                 cube[2][0][0] = tmp1
#                 cube[2][1][0] = tmp2
#                 cube[2][2][0] = tmp3
#                 cube[4] = rotate(4)
#         elif rotation[i][0] == 'R':
#             for _ in range(a):
#                 tmp1 = cube[0][0][2]
#                 tmp2 = cube[0][1][2]
#                 tmp3 = cube[0][2][2]
#                 cube[0][0][2] = cube[2][0][2]
#                 cube[0][1][2] = cube[2][1][2]
#                 cube[0][2][2] = cube[2][2][2]
#                 cube[2][0][2] = cube[1][0][2]
#                 cube[2][1][2] = cube[1][1][2]
#                 cube[2][2][2] = cube[1][2][2]
#                 cube[1][0][2] = cube[3][2][0]
#                 cube[1][1][2] = cube[3][1][0]
#                 cube[1][2][2] = cube[3][0][0]
#                 cube[3][2][0] = tmp1
#                 cube[3][1][0] = tmp2
#                 cube[3][0][0] = tmp3
#                 cube[5] = rotate(5)
#         elif rotation[i][0] == 'U':
#             for _ in range(a):
#                 tmp = cube[2][0]
#                 cube[2][0] = cube[5][0]
#                 cube[5][0] = cube[3][0]
#                 cube[3][0] = cube[4][0]
#                 cube[4][0] = tmp
#                 cube[0] = rotate(0)
#         elif rotation[i][0] == 'D':
#             for _ in range(a):
#                 tmp = cube[2][2]
#                 cube[2][2] = cube[4][2]
#                 cube[4][2] = cube[3][2]
#                 cube[3][2] = cube[5][2]
#                 cube[5][2] = tmp
#                 cube[1] = rotate(1)
#         elif rotation[i][0] == 'F':
#             for _ in range(a):
#                 tmp1, tmp2, tmp3 = cube[0][2][0], cube[0][2][1], cube[0][2][2]
#                 cube[0][2][0] = cube[4][2][2]
#                 cube[0][2][1] = cube[4][1][2]
#                 cube[0][2][2] = cube[4][0][2]
#                 cube[4][2][2] = cube[1][0][2]
#                 cube[4][1][2] = cube[1][0][1]
#                 cube[4][0][2] = cube[1][0][0]
#                 cube[1][0][2] = cube[5][0][0]
#                 cube[1][0][1] = cube[5][1][0]
#                 cube[1][0][0] = cube[5][2][0]
#                 cube[5][0][0] = tmp1
#                 cube[5][1][0] = tmp2
#                 cube[5][2][0] = tmp3
#                 cube[2] = rotate(2)
#         elif rotation[i][0] == 'B':
#             for _ in range(a):
#                 tmp1, tmp2, tmp3 = cube[0][0][0], cube[0][0][1], cube[0][0][2]
#                 cube[0][0][0] = cube[5][0][2]
#                 cube[0][0][1] = cube[5][1][2]
#                 cube[0][0][2] = cube[5][2][2]
#                 cube[5][0][2] = cube[1][2][2]
#                 cube[5][1][2] = cube[1][2][1]
#                 cube[5][2][2] = cube[1][2][0]
#                 cube[1][2][2] = cube[4][2][0]
#                 cube[1][2][1] = cube[4][1][0]
#                 cube[1][2][0] = cube[4][0][0]
#                 cube[4][0][0] = tmp3
#                 cube[4][1][0] = tmp2
#                 cube[4][2][0] = tmp1
#                 cube[3] = rotate(3)
#     for i in range(3):
#         print(''.join(cube[0][i]))