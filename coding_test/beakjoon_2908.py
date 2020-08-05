# 상수

a, b = map(str, input().split())
a = list(a)
b = list(b)
a.reverse()
b.reverse()
print(max(int(''.join(a)), int(''.join(b))))