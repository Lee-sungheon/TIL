# 빙고
def input_bingo(number):
    for i in range(5):
        for j in range(5):
            if bingo[i][j] == number:
                bingo[i][j] = '*'
                return


def check_bingo():
    return

bingo = [list(map(int, input().split())) for _ in range(5)]
num = []
for _ in range(5):
    tmp = list(map(int, input().split()))
    for i in range(5):
        num.append(tmp[i])
print(num)

for k in range(num):
    input_bingo(num[k])
    check_bingo()