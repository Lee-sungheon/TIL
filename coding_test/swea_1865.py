# 동철이의 일 분배

# dfs
def f1(n, k, val):   # n번 사람이 맡을 일의 번호를 결정, n-1번 사람까지의 성공확률 val
    global max_val
    if n == k:
        if max_val < val*100:
            max_val = val*100
        return
    elif max_val >= val*100:
        return
    else:
        for i in range(k):
            if u[i] == 0:   # i번 일을 맡은 사람이 없으면
                u[i] = 1    # i번 일을 배정
                f1(n+1, k, val*P[n][i]/100)  # n+1 번 사람이 맡을 일을 결정, n번 사람이 i번 일을 맡을떄의 성공확률을 곱함
                u[i] = 0    # i번 일을 다른 사람이 맡을 수 있도록 함


# 순열
def f2(n, k, s):
    global max_val
    if n == k:
        if max_val < s*100:
            max_val = s*100
        return
    elif max_val >= s*100:
        return
    else:
        for i in range(n, k):
            p[n], p[i] = p[i], p[n]
            f2(n+1, k, s*P[n][p[n]]/100)
            p[n], p[i] = p[i], p[n]


T = int(input())
for tc in range(T):
    max_val = 0
    N = int(input())
    arr = [i for i in range(N)]
    P = [list(map(int, input().split())) for _ in range(N)]
    u = [0]*N   # u[i] i번 일의 배정 여부
    p = [i for i in range(N)]
    f2(0, N, 1)
    print('#%d %.6f' % (tc+1, round(max_val, 6)))