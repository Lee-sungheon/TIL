delta = [[0, 1], [0, -1], [1, 0], [-1, 0]]
def dfs(row, col, grid, visit, res):
    visit[row][col] = True
    res[-1] = res[-1]+[[row, col]]
    for dx, dy in delta:
        nx = col + dx
        ny = row + dy
        if nx < 0 or ny < 0 or nx >= len(grid) or ny >= len(grid):
            continue
        if grid[ny][nx] == '1' and not visit[ny][nx]:
            dfs(ny, nx, grid, visit, res)


def countMatches(grid1, grid2):
    visited1 = [[False]*grid1_count for _ in range(grid1_count)]
    visited2 = [[False]*grid2_count for _ in range(grid2_count)]
    result1 = []
    result2 = []
    answer = 0
    for i in range(grid1_count):
        for j in range(grid1_count):
            if not visited1[i][j] and grid1[i][j] == '1':
                result1.append([])
                dfs(i, j, grid1, visited1, result1)
    for i in range(grid2_count):
        for j in range(grid2_count):
            if not visited2[i][j] and grid2[i][j] == '1':
                result2.append([])
                dfs(i, j, grid2, visited2, result2)
    result1.sort()
    result2.sort()
    for i in range(len(result1)):
        if result1[i] in result2:
            answer += 1
    return answer

grid1_count = int(input().strip())
grid1 = []
for _ in range(grid1_count):
    grid1_item = input()
    grid1.append(grid1_item)
grid2_count = int(input().strip())
grid2 = []
for _ in range(grid2_count):
    grid2_item = input()
    grid2.append(grid2_item)
result = countMatches(grid1, grid2)
print(result)