# 꼬인 전깃줄
def binary_search(value, low, high):
    mid = (low+high) // 2
    if mid - 1 > 0:
        if result[mid-1] <= value <= result[mid]:
            return mid
        elif result[mid] < value:
            pass
        elif result[mid-1] > value:
            pass

    if array[mid] <= value:
        return binary_search(value, low, mid-1)
    else:
        return binary_search(value, mid+1, high)


N = int(input())
array = list(map(int, input().split()))
result = []
num = -1
idx = 0
for i in range(N):
    if num < array[i]:
        result.append(array[i])
        num = result[-1]
    else:
        binary_search(array[i], 0, len(result)-1)
