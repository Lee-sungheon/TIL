def sd(like, n):
    m = sum(like) / n
    total = 0
    for i in range(n):
        total += (like[i] - m) ** 2
    total = total / n
    result = total ** (1 / 2)
    print(result)
    return result


N, K = map(int, input().split())
likes = list(map(int, input().split()))
answer = 1000000
for j in range(K, N+1):
    for i in range(N-j+1):
        answer = min(answer, sd(likes[i:i+j], j))
print(answer)