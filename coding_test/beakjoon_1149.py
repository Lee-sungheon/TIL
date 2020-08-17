# RGB 거리

N = int(input())
rgbs = [list(map(int, input().split())) for _ in range(N)]
dp = [[0]*3 for _ in range(N)]
dp[0][0] = rgbs[0][0]
dp[0][1] = rgbs[0][1]
dp[0][2] = rgbs[0][2]

for i in range(1, N):
    for j in range(3):
        for k in range(3):
            tmp = 0
            if dp[i][j] == 0 and j != k:
                dp[i][j] = dp[i-1][k] + rgbs[i][j]
                tmp = dp[i-1][k]
            elif dp[i][j] != 0 and j != k:
                dp[i][j] = min(dp[i][j], dp[i-1][k] - tmp + rgbs[i][j])

print(min(dp[N-1]))