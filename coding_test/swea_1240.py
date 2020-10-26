# 단순 2진 암호코드
T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    array = [list(map(int, input())) for _ in range(N)]
    secret = []
    code = [[0, 0, 0, 1, 1, 0, 1], [0, 0, 1, 1, 0, 0, 1], [0, 0, 1, 0, 0, 1, 1], [0, 1, 1, 1, 1, 0, 1],
            [0, 1, 0, 0, 0, 1, 1], [0, 1, 1, 0, 0, 0, 1], [0, 1, 0, 1, 1, 1, 1],
            [0, 1, 1, 1, 0, 1, 1], [0, 1, 1, 0, 1, 1, 1], [0, 0, 0, 1, 0, 1, 1]]
    result = []
    for i in range(N):
        if 1 in array[i]:
            for j in range(M-1, -1, -1):
                if array[i][j] == 1:
                    secret = array[i][j-55:j+1]
                    break
            break
    for i in range(8):
        for j in range(10):
            if secret[7*i:(i+1)*7] == code[j]:
                result.append(j)
    total = (result[0]+result[2]+result[4]+result[6]) * 3 + (result[1]+result[3]+result[5]+result[7])
    if total >= 10 and total % 10 == 0:
        print('#{} {}' .format(tc+1, sum(result)))
    else:
        print('#{} 0' .format(tc+1))
