# 사칙연산
def post_order(idx):
    if idx >= len(tree):
        return
    post_order(idx * 2)
    post_order(idx * 2 + 1)
    cal.append(tree[idx][2])


for tc in range(10):
    N = int(input())
    tree = [[0]*3 for _ in range(N + 1)]
    cal = []
    stack = []
    for _ in range(N):
        tmp = input().split()
        tmp[0] = int(tmp[0])
        if len(tmp) <= 2:
            tree[tmp[0]][2] = int(tmp[1])
        else:
            tree[tmp[0]][2] = tmp[1]
            tree[tmp[0]][0] = int(tmp[2])
            tree[tmp[0]][1] = int(tmp[3])
    for i in range(N, 0, -1):
        if tree[i][2] == '*':
            tree[i][2] = tree[tree[i][0]][2] * tree[tree[i][1]][2]
        elif tree[i][2] == '+':
            tree[i][2] = tree[tree[i][0]][2] + tree[tree[i][1]][2]
        elif tree[i][2] == '-':
            tree[i][2] = tree[tree[i][0]][2] - tree[tree[i][1]][2]
        elif tree[i][2] == '/':
            tree[i][2] = tree[tree[i][0]][2] / tree[tree[i][1]][2]
    print(f'#{tc + 1} {int(tree[1][2])}')