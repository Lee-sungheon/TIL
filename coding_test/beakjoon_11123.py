# 양

import sys
sys.setrecursionlimit(10**7)


def search(sheep, i, j):
    if i+1 < H and sheep[i+1][j] == '#':
        sheep[i+1][j] = 1
        search(sheep, i + 1, j)
    if i-1 >= 0 and sheep[i-1][j] == '#':
        sheep[i-1][j] = 1
        search(sheep, i - 1, j)
    if j+1 < W and sheep[i][j+1] == '#':
        sheep[i][j+1] = 1
        search(sheep, i, j + 1)
    if j-1 >= 0 and sheep[i][j-1] == '#':
        sheep[i][j-1] = 1
        search(sheep, i, j - 1)
    return

T = int(input())
for tc in range(T):
    H, W = map(int, input().split())
    sheep = [list(map(str, input())) for _ in range(H)]
    cnt = 0
    for i in range(H):
        for j in range(W):
            if sheep[i][j] == '#':
                sheep[i][j] = 1
                search(sheep, i, j)
                cnt += 1
    print(cnt)