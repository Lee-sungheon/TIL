# 팩토리얼

N = int(input())
dp = [1]
for i in range(1, N+1):
    dp.append(dp[i-1]*i)
print(dp[-1])
