# 게임

X, Y = map(int, input().split())
Z = int(100*Y/X)
if Z >= 99:
    print(-1)
else:
    left = X
    right = 2*X
    while left <= right:
        mid = (left + right)//2
        if int(100*(mid-X+Y)/mid) > Z:
            right = mid-1
        else:
            left = mid+1
    print(left-X)
