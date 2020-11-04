# 부등식
B2, C2, D2 = map(int, input().split())
A1, A2 = map(int, input().split())
E1, E2 = map(int, input().split())
result = 0
C0 = int(A1/A2*C2) - 1
C1 = int(C2*E1/E2) + 1

for i in range(C0, C1):
    if A1/A2 < i/C2 < E1/E2:
        result += ((B2*i-1)//C2-(B2*A1//A2))*((D2*E1-1)//E2-(D2*i//C2))
print(result)
