# 자리배정

C, R = map(int, input().split())
K = int(input())
if K > C*R:
    print(0)
else:
    matrix = [[0]*R for _ in range(C)]
    delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    x, y = 0, 0
    index = 0
    for i in range(1, C*R+1):
        matrix[y][x] = i
        if i == K:
            print(y+1, x+1)
            break
        if x + delta[index][1] < 0 or y + delta[index][0] < 0 or x + delta[index][1] >= R or y + delta[index][0] >= C:
            index = (index+1) % 4
        elif matrix[y + delta[index][0]][x + delta[index][1]] != 0:
            index = (index+1) % 4
        x += delta[index][1]
        y += delta[index][0]
