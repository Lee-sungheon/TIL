def check(x, y, dep):
    global cnt
    if dep >= cnt:
        return
    if matrix[y][x] == 1:
        for k in range(5, 0, -1):
            if 0 < x+k <= 10 and 0 < y+k <= 10 and recheck(x, y, k) and num[k] > 0:
                change(x, y, k, 0)
                num[k] -= 1
                if x < 9:
                    check(x+1, y, dep+1)
                else:
                    if y < 9:
                        check((x+1) % 10, y+1, dep+1)
                    else:
                        check(x, y, dep+1)
                change(x, y, k, 1)
                num[k] += 1
    else:
        if x < 9:
            check(x+1, y, dep)
        else:
            if y < 9:
                check((x+1) % 10, y+1, dep)
            else:
                for n in range(10):
                    for m in range(10):
                        if matrix[n][m] == 1:
                            return
                else:
                    if cnt > dep:
                        cnt = dep

def recheck(x, y, k):
    for i in range(k):
        for j in range(k):
            if matrix[y+i][x+j] != 1:
                return 0
    return 1


def change(x, y, k, value):
    for i in range(y, y+k):
        for j in range(x, x+k):
            matrix[i][j] = value


matrix = [list(map(int, input().split())) for _ in range(10)]
num = [0, 5, 5, 5, 5, 5]
cnt = 26
check(0, 0, 0)
if cnt == 26:
    print(-1)
else:
    print(cnt)
