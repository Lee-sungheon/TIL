# 엘리베이터 장난

N, m = map(int, input().split())
buttons = set(['0'*N])
time1, time2, time3, time4 = N, N//2, N//2 + N%2, (N-1)//3 + 1
# 1인 경우
if time1 <= m:
    buttons.add('1'*N)
    if time1 + time4 <= m:
        tmp = ['1']*N
        for i in range(N):
            if i%3 == 0:
                tmp[i] = '0'
        buttons.add(''.join(tmp))
# 2인 경우
if time2 <= m and time2 != 0:
    tmp = ['0'] * N
    for i in range(N):
        if i%2 == 0:
            tmp[i] = '1'
    buttons.add(''.join(tmp))
    if time2 + time4 <= m:
        for i in range(N):
            if i%3 == 0:
                tmp[i] = ('0' if tmp[i] == '1' else '1')
        buttons.add(''.join(tmp))
# 3인 경우
if time3 <= m:
    tmp = ['0'] * N
    for i in range(N):
        if i % 2:
            tmp[i] = '1'
    buttons.add(''.join(tmp))
    if time3 + time4 <= m:
        for i in range(N):
            if i%3 == 0:
                tmp[i] = ('0' if tmp[i] == '1' else '1')
        buttons.add(''.join(tmp))
# 4인 경우
if time4 <= m:
    tmp = ['0'] * N
    for i in range(N):
        if i % 3 == 0:
            tmp[i] = '1'
    buttons.add(''.join(tmp))

print(len(buttons))
