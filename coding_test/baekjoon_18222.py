# 투에-모스 문자열

k = int(input())
cnt = 0
while k != 0:
    cnt += 1
    v = 1
    while v*2 < k:
        v *= 2
    k = k-v
if cnt%2 == 1:
    print(0)
else:
    print(1)