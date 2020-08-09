# 덩치

N = int(input())
bodys = [list(map(int, input().split())) for _ in range(N)]
body_rank = [1]*N

for i in range(len(bodys)):
    for j in range(len(bodys)):
        if bodys[i][0] < bodys[j][0] and bodys[i][1] < bodys[j][1]:
            body_rank[i] += 1

for rank in body_rank:
    print(rank, end=' ')