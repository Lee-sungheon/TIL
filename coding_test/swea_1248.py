# 공통조상
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
    V, E, son1, son2 = map(int, input().split())
    nodes = list(map(int, input().split()))
    tree = [[0] * 3 for _ in range(V + 1)]
    ancestor1, ancestor2 = [], []
    for i in range(E):
        p, c = nodes[i * 2], nodes[i * 2 + 1]
        if tree[p][0] == 0:
            tree[p][0] = c
        else:
            tree[p][1] = c
        tree[c][2] = p
    while son1 > 0 or son2 > 0:
        son1, son2 = tree[son1][2], tree[son2][2]
        ancestor1.append(son1)
        ancestor2.append(son2)
    common = 0
    for anc in ancestor1:
        if anc in ancestor2:
            common = anc
            break
    cnt = 1
    subtree(common)
    print(f'#{tc+1} {common} {cnt}')