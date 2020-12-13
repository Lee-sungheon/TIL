# [모의 SW 역량테스트] 요리사
def combinations(v, s):
    if v == m:
        com.append(tuple(res))
    else:
        for i in range(s, n):
            res[v] = i
            combinations(v + 1, i + 1)


T = int(input())
for tc in range(T):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    n = N
    m = N//2
    com = []
    res = [0] * m
    combinations(0, 0)
    final_com = []
    for i in range(len(com)):
        tmp = {i for i in range(N)}
        tmp = tuple(tmp - set(com[i]))
        final_com.append((com[i], tmp))

    final_com = final_com[:len(final_com)//2]
    result = 2000000000
    for i in range(len(final_com)):
        s1 = s2 = 0
        for j in range(N//2):
            for k in range(N//2):
                s1 += matrix[final_com[i][0][j]][final_com[i][0][k]]
                s2 += matrix[final_com[i][1][j]][final_com[i][1][k]]
        tmp = abs(s1-s2)
        if tmp < result:
            result = tmp
    print("#{} {}" .format(tc+1, result))
