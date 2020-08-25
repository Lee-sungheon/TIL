T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    flag = [input() for _ in range(N)]

    min_num = []
    for i in range(N-2):
        for j in range(i+1, N-1):
            s1 = s2 = s3 = 0
            for k in range(0, i+1):
                s1 += (M - flag[k].count('W'))
            for k in range(i+1, j+1):
                s2 += (M - flag[k].count('B'))
            for k in range(j+1, N):
                s3 += (M - flag[k].count('R'))
            min_num.append(s1 + s2 + s3)
    
    print(f'#{tc+1} {min(min_num)}')