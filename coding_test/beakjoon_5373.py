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
            cube[0][0]