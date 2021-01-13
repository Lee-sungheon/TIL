# Flood-It

T = int(input())
delta = ((1, 0), (0, 1), (-1, 0), (0, -1))
for tc in range(T):
    N = int(input())
    game = [list(map(int, input())) for _ in range(N)]
    cnt = [0]*6
    result = 0
    visited = [[False]*N for _ in range(N)]
