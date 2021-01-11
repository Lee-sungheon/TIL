# 쿼드압축 후 개수 세기(lv.2)
import numpy as np


def solution(arr):
    global cnt
    n = len(arr)
    if n == 1:
        cnt[arr[0]] += 1
        return
    else:
        n = n//2

    cnt2 = [0, 0]
    for i in range(2):
        for j in range(2):
            tmp = arr[i * n][j * n]
            arr = np.array(arr)
            tmp_arr = arr[i*n:(i+1)*n, j*n:(j+1)*n]
            tmp_arr = tmp_arr.tolist()
            tmp_cnt = 0
            for k in range(n):
                if tmp_arr[k].count(tmp) != n:
                    break
                else:
                    tmp_cnt += 1
            if tmp_cnt == n:
                cnt[tmp] += 1
                cnt2[tmp] += 1
            else:
                solution(tmp_arr)
    else:
        if cnt2[0] == 4:
            cnt[0] -= 3
        if cnt2[1] == 4:
            cnt[1] -= 3
    return


cnt = [0, 0]
array = [[1,1,1,1], [1,1,1,1], [1,1,1,1], [1,1,1,1]]
solution(array)
print(cnt)
