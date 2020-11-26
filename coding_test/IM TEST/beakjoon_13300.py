# 방 배정

N, K = map(int, input().split())
girls = [0]*6
boys = [0]*6
for _ in range(N):
    i, n = map(int, input().split())
    if i == 0:
        girls[n-1] += 1
    else:
        boys[n-1] += 1
cnt = 0
for i in range(6):
    cnt += (girls[i] + (K-1)) // K
    cnt += (boys[i] + (K-1)) // K
print(cnt)