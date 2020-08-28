# 종이 붙이기
T = int(input())
for tc in range(T):
    n = int(input()) // 10
    dp = [0] * (n+1)
    if n == 1:
        print(f'#{tc+1} 1')
    elif n == 2:
        print(f'#{tc+1} 3')
    else:
        dp[1] = 1
        dp[2] = 3
        for i in range(3, n+1):
            dp[i] = dp[i-1] + 2*dp[i-2]
        print(f'#{tc+1} {dp[n]}')
