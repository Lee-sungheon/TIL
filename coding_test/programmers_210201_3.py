# 멀쩡한 사각형

import math
def solution(w,h):
    x = 0
    a = max(w, h)
    b = min(w, h)
    for i in range(1, b+1):
        x += (math.ceil(a*i/b) - math.floor(a*(i-1)/b))
    answer = a * b - x
    return answer