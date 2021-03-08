# 개업 2

N, M = map(int, input().split())
tools = list(map(int, input().split()))
totals = []
for i in range(M):
    totals.append(tools[i])
    for j in range(M):
        if i != j:
            totals.append(tools[i] + tools[j])
totals = sorted(list(set(totals)))

dp = [N+1 for _ in range(N+1)]
dp[0] = 0
for i in range(1, N+1):
    for j in totals:
        if i - j < 0:
            break
        dp[i] = min(dp[i], dp[i-j]+1)
if dp[-1] >= N+1:
    print(-1)
else:
    print(dp[-1])