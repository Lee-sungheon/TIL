# SWEA_2819
def search(x, y, depth, val):
    delta = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    if depth == 7:
        result.add(val)
        return
    for dx, dy in delta:
        nx, ny = x + dx, y + dy
        if nx < 0 or ny < 0 or nx >= 4 or ny >= 4:
            continue
        search(nx, ny, depth+1, 10*val+lattice[ny][nx])


T = int(input())
for tc in range(T):
    result = set()
    lattice = [list(map(int, input().split())) for _ in range(4)]
    for i in range(4):
        for j in range(4):
            search(j, i, 1, lattice[i][j])
    print(f'#{tc+1} {len(result)}')
