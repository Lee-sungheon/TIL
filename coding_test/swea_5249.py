# 최소 신장 트리
def make_set(v):
    parent[v] = v
    rank[v] = 0


def find(v):
    if parent[v] != v:
        parent[v] = find(parent[v])
    return parent[v]


def union(v, u):
    root1 = find(v)
    root2 = find(u)
    if root1 != root2:
        if rank[root1] > rank[root2]:
            parent[root2] = root1
        else:
            parent[root1] = root2
            if rank[root1] == rank[root2]:
                rank[root2] += 1


def kruskal(graph):
    for v in vertices:
        make_set(v)
    graph.sort()
    for edge in graph:
        weight, v, u = edge
        if find(v) != find(u):
            union(v, u)
            mst.append(edge)
    return


T = int(input())
for tc in range(T):
    mst = []
    parent = {}
    rank = {}
    V, E = map(int, input().split())
    vertices = [i for i in range(V+1)]
    graph = []
    for i in range(E):
        a, b, c = map(int, input().split())
        graph.append((c, a, b))
    result = 0
    for a, b, c in kruskal(graph):
        result += a
    print(graph)
    print('#{} {}' .format(tc+1, result))