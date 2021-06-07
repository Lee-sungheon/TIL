# 직사각형에서 탈출

x, y, w, h = map(int, input().split())
print(min(abs(x-w), abs(y-h), abs(x), abs(y)))