# 재미있는 오셀로 게임

T = int(input())
delta = [[0, 1], [1, 0], [-1, 0], [0, -1], [1, 1], [-1, 1], [-1, -1], [1, -1]]

for tc in range(T):
    N, M = map(int, input().split())
    matrix = [[0] * N for _ in range(N)]
    matrix[N // 2 - 1][N // 2 - 1] = matrix[N // 2][N // 2] = 2
    matrix[N // 2 - 1][N // 2] = matrix[N // 2][N // 2 - 1] = 1

    for i in range(M):
        place = list(map(int, input().split()))
        place[0] -= 1
        place[1] -= 1
        matrix[place[0]][place[1]] = place[2]
        change = []

        for i in range(8):
            dx, dy = delta[i]
            x, y = place[0] + dx, place[1] + dy
            while True:
                if x < 0 or y < 0 or x > N - 1 or y > N - 1:
                    change = []
                    break
                if matrix[x][y] == 0:
                    change = []
                    break
                if matrix[x][y] == place[2]:
                    break
                change.append([x, y])
                x, y = x + dx, y + dy
            for cx, cy in change:
                if place[2] == 1:
                    matrix[cx][cy] = 1
                else:
                    matrix[cx][cy] = 2

    white = black = 0
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 1:
                black += 1
            elif matrix[i][j] == 2:
                white += 1
    print(f'#{tc + 1} {black} {white}')