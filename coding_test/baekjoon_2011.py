# 암호코드

code = input()
n = len(code)
dp = [0] * (n+1)
dp[0], dp[1] = 1, 1
if code[0] == '0':
    dp[1] = 0
for i in range(2, n+1):
    tmp = int(code[i-1])
    if 0 < tmp < 10:
        dp[i] += dp[i-1]
    tmp = int(code[i-2])*10 + int(code[i-1])
    if 9 < tmp < 27:
        dp[i] = (dp[i] + dp[i-2])
print(dp[n] % 1000000)
