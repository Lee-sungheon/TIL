# 스도쿠 검증

T = int(input())
for tc in range(T):
    result = 1
    sudoku = [list(map(int, input().split())) for _ in range(9)]
    for i in range(9):
        tmp = []
        tmp2 = []
        for j in range(9):
            tmp.append(sudoku[j][i])
            tmp2.append(sudoku[3*(i//3)+(j//3)][3*(i%3)+(j%3)])
        if len(set(sudoku[i])) < 9 or len(set(tmp)) < 9 or len(set(tmp2)) < 9:
            result = 0
            break
    
    print('#%d' %(tc+1), result)