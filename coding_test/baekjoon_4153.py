# 직각삼각형

while True:
    tmp = list(map(int, input().split()))
    tmp.sort()
    a, b, c = tmp
    if a == 0 and b == 0 and c == 0:
        break
    if a**2 + b**2 == c**2:
        print("right")
    else:
        print("wrong")