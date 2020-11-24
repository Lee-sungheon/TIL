# 이진탐색
def binary_search(arr, l, r, value, dir):
    global result
    if l > r:
        return
    m = (l+r) // 2
    if arr[m] == value:
        result += 1
        return
    elif arr[m] < value:
        if dir == 1 or dir == 2:
            binary_search(arr, m+1, r, value, 0)
        else:
            return
    else:
        if dir == 0 or dir == 2:
            binary_search(arr, l, m-1, value, 1)
        else:
            return


T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    B = list(map(int, input().split()))
    result = 0
    for i in range(N):
        if A[i] in B:
            binary_search(A, 0, N-1, A[i], 2)
    print('#{} {}' .format(tc+1, result))
