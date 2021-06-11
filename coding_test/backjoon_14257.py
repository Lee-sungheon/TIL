# XOR 방정식
def bitwiseEquations(a, b):
    if a < b:
        print(0)
    else:
        dif = a - b
        cnt = 0
        for i in range(41, -1, -1):
            if b & (1 << i):
                cnt += 1
            elif dif >= (1 << i) * 2:
                dif -= (1 << i) * 2
        if dif == 0:
            if a == b:
                print(2**cnt - 2)
            else:
                print(2**cnt)
        else:
            print(0)
    return


S, X = map(int, input().split())
bitwiseEquations(S, X)