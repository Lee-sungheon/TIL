# 호텔

def dpdp(N, C):
    for i in range(N):
        for j in range(1, C+1):
            dp[0] = 0
            s = j - hotels[i][1]
            if s <= 0:
                s = 0
            if dp[j] == -1:
                dp[j] = dp[s] + hotels[i][0]
            else:
                dp[j] = min(dp[j], dp[s] + hotels[i][0])
    return dp


C, N = map(int, input().split())
hotels = [list(map(int, input().split())) for _ in range(N)]
dp = [-1]*(C+1)
print(dpdp(N, C)[C])