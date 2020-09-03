# SWEA_1238
def bfs(S):
    visited = [0] * 101
    queue = [(S, 0)]
    result = [(S, 0)]
    visited[S] = 1
    while queue:
        s, cnt = queue.pop(0)
        for e in range(1, 101):
            if matrix[s][e] != 0 and visited[e] == 0:
                queue.append((e, cnt + 1))
                visited[e] = 1
                result.append((e, cnt + 1))
    max_num = result_num = 0
    print(result)
    for i in range(len(result)):
        if result[i][1] > max_num:
            max_num = result[i][1]
    for i in range(len(result)):
        if result[i][1] == max_num and result[i][0] > result_num:
            result_num = result[i][0]
    return result_num


for tc in range(10):
    N, S = map(int, input().split())
    matrix = [[0]*101 for _ in range(101)]
    tmp = list(map(int, input().split()))
    for i in range(N//2):
        x, y = tmp[i*2], tmp[i*2+1]
        matrix[x][y] = 1
    print(f'#{tc+1} {bfs(S)}')