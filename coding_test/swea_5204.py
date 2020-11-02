# 병합 정렬
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)


def merge(left, right):
    global result
    i = j = 0
    sorted_arr = []
    if left[-1] > right[-1]:
        result += 1
    while (i < len(left)) & (j < len(right)):
        if left[i] < right[j]:
            sorted_arr.append(left[i])
            i += 1
        else:
            sorted_arr.append(right[j])
            j += 1
    while i < len(left):
        sorted_arr.append(left[i])
        i += 1
    while j < len(right):
        sorted_arr.append(right[j])
        j += 1
    return sorted_arr


T = int(input())
for tc in range(T):
    N = int(input())
    array = list(map(int, input().split()))
    result = 0
    array = merge_sort(array)
    print('#{} {} {}' .format(tc+1, array[N//2], result))
