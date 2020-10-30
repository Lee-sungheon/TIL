# 친구 네트워크
import sys
# T = int(input())
# for tc in range(T):
#     F = int(input())
#     set_li = []
#     for i in range(F):
#         a, b = input().split()
#         tmp = []
#         cnt = 0
#         result = 2
#         for j in range(len(set_li)):
#             if a in set_li[j] or b in set_li[j]:
#                 set_li[j].add(a)
#                 set_li[j].add(b)
#                 tmp.append(j)
#                 cnt += 1
#                 result = len(set_li[j])
#                 if len(tmp) == 2:
#                     set_li[tmp[0]] = set_li[tmp[0]] | set_li[tmp[1]]
#                     del set_li[tmp[1]]
#                     result = len(set_li[tmp[0]])
#                     break
#         else:
#             if not cnt:
#                 set_li.append({a, b})
#         print(result)


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
    parents[b] = a


T = int(input())
for _ in range(T):
    F = int(input())
    parents = {}
    cnt = {}
    for _ in range(F):
        x1, x2 = map(str, sys.stdin.readline().split())
        if x1 not in parents:
            parents[x1] = x1
            cnt[x1] = 1
        if x2 not in parents:
            parents[x2] = x2
            cnt[x2] = 1
        union(x1, x2)
        print((cnt[find(parents[x1])]))
