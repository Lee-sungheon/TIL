# 타일
N = int(input())
K = int(input())
if N % 2 == 0:
    zero = N//2 + 1
else:
    zero = N//2
for i in range(K):
    a, b = map(int, input().split())
    if b <= zero < a:
        a = N - a + 1
    elif a <= zero < b:
        b = N - b + 1
    elif a > zero and b > zero:
        a, b = N - a + 1, N - b + 1
    print((min(a, b)-1) % 3 + 1)