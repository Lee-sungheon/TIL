# 함수 : 정수 N개의 합

def solve(a: list):
    total = 0
    for i in a:
        total += i
    return int(total)

print(solve([1,2,3,4,5]))