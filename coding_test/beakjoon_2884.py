#알람 시계

H,M=map(int,input().split())
if (45<=M):
    print(f"{H} {M-45}")
else:
    M = M+15
    if (H==0):
        H=23
    else:
        H=H-1
    print(f"{H} {M}")