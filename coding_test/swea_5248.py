# 그룹 나누기
def find(x):
    if parents[x] == x:
        return x
    parents[x] = find(parents[x])
    return parents[x]


def union(a, b):
    a = find(a)
    b = find(b)
    if a != b:
        cnt[a] += cnt[b]
        del cnt[b]
    parents[b] = a


T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    array = list(map(int, input().split()))
    parents = {}
    cnt = {}
    for i in range(M):
        x1, x2 = array[i * 2], array[i * 2 + 1]
        if x1 not in parents:
            parents[x1] = x1
            cnt[x1] = 1
        if x2 not in parents:
            parents[x2] = x2
            cnt[x2] = 1
        union(x1, x2)
    print(parents)
    print(cnt)
    print('#{} {}'.format(tc + 1, N - len(parents) + len(cnt)))
