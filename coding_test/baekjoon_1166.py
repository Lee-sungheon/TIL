# 선물 (Binary search)

N, L, W, H = map(int, input().split())
l, r = 0, min(L, W, H)
for i in range(60):
    m = (l + r) / 2
    if (L//m) * (W//m) * (H//m) < N:
        r = m
    else:
        l = m
print(l)
