# 개미
w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())
np, nq = t % (w*2), t % (h*2)
d = 1
for _ in range(np):
    if p + d > w:
        d = -1
    if p + d < 0:
        d = 1
    p += d
d = 1
for _ in range(nq):
    if q + d > h:
        d = -1
    if q + d < 0:
        d = 1
    q += d
print(f'{p} {q}')
