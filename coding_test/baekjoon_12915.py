# 대회 개최

pro = list(map(int, input().split()))
problems = [pro[0], pro[2], pro[4]]
pro[0] = pro[2] = pro[4] = 0
cnt = 0

while True:
    if problems[0] > 0 and problems[1] > 0 and problems[2] > 0:
        cnt += 1
        problems[0] -= 1
        problems[1] -= 1
        problems[2] -= 1
    if problems[0] == 0:
        if pro[1] > 0:
            problems[0] += 1
            pro[1] -= 1
        else:
            break
    if problems[2] == 0:
        if pro[3] > 0:
            problems[2] += 1
            pro[3] -= 1
        else:
            break
    if problems[1] == 0:
        max_value = max(pro[1], pro[3])
        if max_value > 0:
            if pro[1] != pro[3]:
                pro[pro.index(max_value)] -= 1
            else:
                if problems[0] > problems[2]:
                    pro[1] -= 1
                else:
                    pro[3] -= 1
            problems[1] += 1
        else:
            break
print(cnt)


