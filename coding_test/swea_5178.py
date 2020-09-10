# 노드의 합
T = int(input())
for tc in range(T):
    N, M, L = map(int, input().split())
    tree = [0 for _ in range(N + 1)]
    for _ in range(M):
        idx, num = map(int, input().split())
        tree[idx] = num

    print(f'#{tc+1} {tree[L]}')