# 회의실 배정 2, 회의실 배정 3
import sys

input = sys.stdin.readline
N = int(input())
rooms = [list(map(int, input().split())) for _ in range(N)]
if N == 1:
    print(rooms[0][2])
else:
    dp = [[0, 0] for _ in range(N)]
    dp[0][1] = rooms[0][2]
    dp[1][1] = rooms[1][2]
    dp[1][0] = rooms[0][2]
    for i in range(2, N):
        dp[i][0] = max(dp[i-1][0], dp[i-1][1])
        dp[i][1] = dp[i-1][0] + rooms[i][2]
    print(max(dp[N-1]))