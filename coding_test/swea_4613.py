# SWEA_4613

def combinations(v, s):
    if v == 2:
        result.append(tuple(res))
    else:
        for i in range(s, n):
            res[v] = i
            combinations(v + 1, i + 1)


T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    flag = [input() for _ in range(N)]

    n = N   # 범위
    result = []
    res = [0] * 2   # 뽑을 조합 개수
    combinations(0, 1)  # 1부터 시작

    min_num = []
    for i, j in result:
        s1 = s2 = s3 = 0
        for k in range(0, i):
            s1 += (M - flag[k].count('W'))
        for k in range(i, j):
            s2 += (M - flag[k].count('B'))
        for k in range(j, N):
            s3 += (M - flag[k].count('R'))
        min_num.append(s1 + s2 + s3)

    print(f'#{tc + 1} {min(min_num)}')
