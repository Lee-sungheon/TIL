# 별 찍기 - 13

n = int(input())
for i in range(n):
    print('*'*(i+1))
for i in range(n-1, 0, -1):
    print('*'*(i))