# 배열 탐색

T = int(input())
for tc in range(T):
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    result = []
    # 배열 찾기
    for i in range(n):
        for j in range(n):
            if matrix[i][j] != 0:
                x = y = 0
                for k in range(j, n):
                    if matrix[i][k]:
                        x += 1
                    else:
                        break
                for k in range(i, n):
                    if matrix[k][j]:
                        y += 1
                    else:
                        break
                result.append([x, y, x*y])

                for k in range(i, i+y):
                    for l in range(j, j+x):
                        matrix[k][l] = 0
    # 버블 솔트
    for i in range(len(result) - 1):
        for j in range(len(result) - i - 1):
            if result[j][2] > result[j+1][2]:
                result[j], result[j+1] = result[j+1], result[j]
    # 버블 솔트는 정렬 과정에서 인자 위치가 바껴서 다시 정렬이 필요
    for i in range(len(result) - 1):
        if result[i][2] == result[i+1][2] and result[i][1] > result[i+1][1]:
            result[i], result[i+1] = result[i+1], result[i]
    # 출력
    print(f'#{tc + 1} {len(result)}', end='')
    for i in range(len(result)):
        print(f' {result[i][1]} {result[i][0]}', end='')
    print()