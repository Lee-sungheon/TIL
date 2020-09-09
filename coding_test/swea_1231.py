# 중위순회
def preorder(node):
    if node:
        preorder(tree[node][0])
        print(tree[node][2], end="")
        preorder(tree[node][1])


for tc in range(10):
    V = int(input())
    tree = [[0] * 3 for _ in range(V + 1)]
    for i in range(1, V+1):
        input_list = input().split()
        idx = int(input_list[0])
        tree[idx][2] = input_list[1]
        if len(input_list) > 2:
            for j in range(len(input_list) - 2):
                tree[idx][j] = int(input_list[j+2])
    print(f'#{tc+1} ', end="")
    preorder(1)
    print()