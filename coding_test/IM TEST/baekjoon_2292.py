# 벌집 (수학)

N = int(input())
x = 0

while True:
    if N >= (3*x*(x+1) + 2):
        x += 1
    else:
        break

print(x+1)
