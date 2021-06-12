# 트리
def dfs(root):
    global result
    if not tree[root]:
        result += 1
        return
    for x in tree[root]:
        dfs(x)


N = int(input())
nodes = list(map(int, input().split()))
tree = [[] for _ in range(N)]
delete = int(input())
result = 0
for i in range(N):
    p = nodes[i]
    if p == -1:
        root = i
        continue
    if i == delete:
        continue
    tree[nodes[i]].append(i)
if root != delete:
    dfs(root)
print(tree)
print(result)
