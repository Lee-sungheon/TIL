# 빙고
def input_bingo(number):
    for i in range(5):
        for j in range(5):
            if bingo[i][j] == number:
                bingo[i][j] = '*'
                return


def check_bingo():
    cnt = 0
    check1 = check2 = 0
    for i in range(5):
        if bingo[i].count('*') == 5:
            cnt += 1
        if bingo[i][i] == '*':
            check1 += 1
        if bingo[i][4-i] == '*':
            check2 += 1
        check3 = 0
        for j in range(5):
            if bingo[j][i] == '*':
                check3 += 1
        if check3 == 5:
            cnt += 1
    if check1 == 5:
        cnt += 1
    if check2 == 5:
        cnt += 1
    return cnt


bingo = [list(map(int, input().split())) for _ in range(5)]
num = []
for _ in range(5):
    tmp = list(map(int, input().split()))
    for i in range(5):
        num.append(tmp[i])
for k in range(25):
    input_bingo(num[k])
    if check_bingo() >= 3:
        print(k+1)
        break