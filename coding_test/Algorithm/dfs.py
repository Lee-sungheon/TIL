'''
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''
def dfs(v):
    # 방문체크
    visited[v] = 1
    print(v, end="")
    # v 의 인접한 정점중에서 방문 안한 정점을 재귀 호출
    for w in range(1, N+1):
        if G[v][w] == 1 and visited[w] == 0:
            dfs(w)

    # stack = list()
    # stack.append(v)
    # while stack:
    #     current = stack[-1]
    #     # 현재 노드에서 갈 수 있는 모든 노드 검사
    #     for i in range(len(G[current])):
    #         # 현재 노드와 연결되어 있고 방문하지 않는 노드라면,
    #         if G[current][i] == 1 and visited[i] == 0:
    #             stack.append(i) # 다음 방문 추가
    #             break

# 정점, 간선
N, E = map(int, input().split())
# 간선들
temp = list(map(int, input().split()))
# 인접행렬
G = [[0] * (N+1) for _ in range(N+1)]
# 방문체크
visited = [0] * (N+1)

# 간선들을 인접행렬에 저장
for i in range(E):
    s, e = temp[2*i], temp[2*i+1]
    G[s][e] = 1
    G[e][s] = 1

dfs(1)