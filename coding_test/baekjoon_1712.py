# 손익분기점

A, B, C = map(int, input().split())
i = 1
if B >= C:
    i = -1
else:
    i = A//(C-B) + 1
          
print(i)