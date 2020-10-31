# 화물 도크

T = int(input())
for tc in range(T):
    N = int(input())
    result = 1
    times = [list(map(int, input().split()))[::-1] for _ in range(N)]
    times.sort()
    time = times[0][0]
    for i in range(1, N):
        if time <= times[i][1]:
            result += 1
            time = times[i][0]
    print('#{} {}' .format(tc+1, result))
