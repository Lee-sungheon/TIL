# subtree
def subtree(n):
    global cnt
    if tree[n][0] != 0:
        cnt += 1
        subtree(tree[n][0])
    if tree[n][1] != 0:
        cnt += 1
        subtree(tree[n][1])


T = int(input())
for tc in range(T):
    E, N = map(int, input().split())
    nodes = list(map(int, input().split()))
    tree = [[0] * 2 for _ in range(max(nodes) + 1)]
    cnt = 1
    for i in range(E):
        p, c = nodes[i * 2], nodes[i * 2 + 1]
        if tree[p][0] == 0:
            tree[p][0] = c
        else:
            tree[p][1] = c

    subtree(N)
    print(f'#{tc+1} {cnt}')