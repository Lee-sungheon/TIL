import sys, math
from decimal import Decimal


N, K = map(int, sys.stdin.readline().split())
dolls = list(map(int, sys.stdin.readline().split()))
sum_s = [0] * (N+1)
st_s = [0] * (N+1)

# O(N^2)로 풀어야함

for i in range(1, N+1):
    sum_s[i] = sum_s[i-1] + dolls[i-1]
    st_s[i] = st_s[i-1] + dolls[i-1] ** 2

min_v = 10000000000
for i in range(K, N+1):     # K 이상
    for j in range(N-i+1):  # 1개씩 증가
        av = Decimal(sum_s[i+j] - sum_s[j]) / i
        st = Decimal(st_s[i+j] - st_s[j]) / i - (av*av)
        min_v = min(min_v, st)
print(min_v.sqrt())