# 수열

N, K = map(int, input().split())
temp_li = list(map(int, input().split()))
sum_li = [sum(temp_li[0:K])]
for i in range(1, N-K+1):
    sum_li.append(sum_li[i-1] + temp_li[i+K-1] - temp_li[i-1])
print(max(sum_li))