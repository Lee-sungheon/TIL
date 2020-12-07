# K번째 수 찾는 함수(정렬)
import sys


def kth(a, k):
    def quick_select(arr, k):
        pivot = arr[(len(arr) + 1) // 2 - 1]
        left, mid, right = [], [], []
        for i in range(len(arr)):
            if arr[i] < pivot:
                left.append(arr[i])
            elif arr[i] > pivot:
                right.append(arr[i])
            else:
                mid.append(arr[i])

        if k < len(left):
            return quick_select(left, k)
        elif k < len(left) + len(mid):
            return mid[0]
        else:
            return quick_select(right, k - len(left) - len(mid))
    k -= 1
    return quick_select(a, k)


N, K = map(int, input().split())
A = list(map(int, sys.stdin.readline().split()))
print(kth(A, K))