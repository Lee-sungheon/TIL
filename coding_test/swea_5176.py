# 이진탐색
def inorder(node):
    if node <= N:
        inorder(node*2)
        tree[node] = tmp.pop(0)
        inorder(node*2+1)


T = int(input())
for tc in range(10):
    N = int(input())
    tree = [0 for _ in range(N + 1)]
    tmp = [i for i in range(1, N+1)]

    inorder(1)
    print(f'#{tc+1} {tree[1]} {tree[N//2]}')