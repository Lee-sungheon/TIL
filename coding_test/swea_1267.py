# 작업순서
def dfs():
    while True:
        if len(result) == V:
            break
        starts = []
        for i in range(1, V+1):
            if 1 not in matrix[i] and i not in result:
                starts.append(i)
        for start in starts:
            result.append(start)
            for j in range(1, V+1):
                matrix[j][start] = 0


for tc in range(10):
    V, E = map(int, input().split())
    matrix = [[0]*(V+1) for _ in range(V+1)]
    tmp = list(map(int, input().split()))
    result = []
    for i in range(E):
        s, e = tmp[i*2], tmp[i*2+1]
        matrix[e][s] = 1
    print(f'#{tc+1} ', end='')
    dfs()
    print(*result)
