# 어린왕자

T = int(input())
for tc in range(T):
    x1, y1, x2, y2 = map(int, input().split())
    N = int(input())
    cnt = 0
    for _ in range(N):
        cx, cy, r = map(int, input().split())
        if (cx-x1)**2 + (cy-y1)**2 <= r**2 and (cx-x2)**2 + (cy-y2)**2 >= r**2:
            cnt += 1
        if (cx-x1)**2 + (cy-y1)**2 >= r**2 and (cx-x2)**2 + (cy-y2)**2 <= r**2:
            cnt += 1
    print(cnt)