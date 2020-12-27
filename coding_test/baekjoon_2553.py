# 마지막 팩토리얼 수
N = int(input())
result = 1
for i in range(1, N+1):
    result *= i

tmp = list(str(result))
for i in range(len(tmp)-1, -1, -1):
    if tmp[i] != '0':
        print(tmp[i])
        break