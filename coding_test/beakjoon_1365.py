# 꼬인 전깃줄
import bisect, sys


def bisect_left(arr, value, begin, end):
    if begin >= end:
        return begin
    mid = begin + (end - begin) // 2
    if arr[mid] < value:
        return bisect_left(arr, value, mid + 1, end)
    else:
        return bisect_left(arr, value, begin, mid)


N = int(input())
array = list(map(int, sys.stdin.readline().split()))
result = [array[0]]
for i in range(N):
    if result[-1] < array[i]:
        result.append(array[i])
    else:
        result[bisect_left(result, array[i], 0, len(result))] = array[i]
print(N-len(result))