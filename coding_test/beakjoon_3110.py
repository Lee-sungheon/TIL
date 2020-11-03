# 부등식
def change(x):
    if x > int(x):
        return int(x)
    else:
        return int(x) - 1


B2, C2, D2 = map(int, input().split())
A1, A2 = map(int, input().split())
E1, E2 = map(int, input().split())
result = 0
C0 = int(A1/A2*C2) - 1
C1 = int(C2*E1/E2) + 1

for i in range(C0, C1):
    A = A1/A2*B2
    Cs = i/C2*B2
    A = change(A)
    Cs = change(Cs)
    E = E1/E2*D2
    Ce = i/C2*D2
    Ce = change(Ce)
    E = change(E)
    if A1/A2 < i/C2 < E1/E2:
        result += (Cs-A)*(E-Ce)
print(result)


