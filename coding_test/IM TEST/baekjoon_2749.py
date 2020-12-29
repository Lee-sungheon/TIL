# 피보나치 수

F = [0, 1]
i = 1
n = int(input())
while True:
    i += 1
    F.append((F[i-1]+F[i-2])%1000000)
    if F[i] == 1:
        if F[i-1] == 0:
            break
print(F[n%(i-1)])