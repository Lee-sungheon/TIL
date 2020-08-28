# 그래프 경로
T = int(input())
for tc in range(1, T+1):
    def dfs(v):
        # visited[v] = 1
        # for w in range(1, N + 1):
        #     if matrix[v][w] == 1 and visited[w] == 0:
        #         dfs(w)

        stack = list()
        stack.append(v)
        visited[v] = 1  # 첫번째 노드는 stack에 추가하면서 방문
        while stack:
            current = stack[-1]
            # 현재 노드에서 갈 수 있는 모든 노드 검사
            visited[current] = 1
            for i in range(len(matrix[current])):
                # 현재 노드와 연결되어 있고 방문하지 않은 노드라면,
                if matrix[current][i] == 1 and visited[i] == 0:
                    stack.append(i)  # 다음방문추가
                    break
            else:  # break에 걸리지 않음 : 현재노드에서 갈수 있는 노드가 없음
                stack.pop()

    result = []
    N, E = map(int, input().split())
    matrix = [[0] * (N + 1) for _ in range(N + 1)]
    visited = [0] * (N + 1)

    for i in range(E):
        s, e = map(int, input().split())
        # 단방향
        matrix[s][e] = 1
    S, G = map(int, input().split())

    dfs(S)
    if visited[G] == 1:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')