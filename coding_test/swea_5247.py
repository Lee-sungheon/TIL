# 연산
from collections import deque


def bfs(dep, n):
    global result
    q = deque()
    q.append((dep, n))
    visited = set()
    while q:
        tmp = q.popleft()
        dn = tmp[1]
        if dn == M:
            return tmp[0]
        if dn in visited:
            continue
        visited.add(dn)
        if 0 < dn*2 <= 1000000:
            q.append((tmp[0]+1, dn*2))
        if 0 < dn+1 <= 1000000:
            q.append((tmp[0]+1, dn+1))
        if 0 < dn-1 <= 1000000:
            q.append((tmp[0]+1, dn-1))
        if 0 < dn-10 <= 1000000:
            q.append((tmp[0]+1, dn-10))


T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    result = M
    print('#{} {}' .format(tc+1, bfs(0, N)))