# 인형들
def sd(l):
    m = sum(l) / len(l)
    t = sum([(k - m) * (k - m) for k in l]) / len(l)
    return t ** 0.5


N, K = map(int, input().split())
like = list(map(int, input().split()))
a = []
for j in range(K):
    for i in range(N-j+1-K):
        a.append(sd(like[i:K+i+j]))
print(min(a))
