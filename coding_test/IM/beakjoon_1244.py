# 스위치 켜고 끄기
T = int(input())
switch = list(map(int, input().split()))
N = int(input())
for _ in range(N):
    x, y = map(int, input().split())
    tmp = y
    if x == 1:
        while y <= T:
            switch[y-1] = (switch[y-1] + 1) % 2
            y = y + tmp
    else:
        switch[y-1] = (switch[y-1] + 1) % 2
        for i in range(1, min(y-1, T-y) + 1):
            if switch[y-1-i] == switch[y-1+i]:
                switch[y-1-i] = (switch[y-1-i] + 1) % 2
                switch[y-1+i] = (switch[y-1+i] + 1) % 2
            else:
                break

for i in range((T-1)//20 + 1):
    print(*switch[20*i:20*i+20])
