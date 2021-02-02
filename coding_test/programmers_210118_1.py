# 야근 지수
import heapq


def solution(n, works):
    le = len(works)
    heap = []
    for work in works:
        heapq.heappush(heap, [-work, work])
    while n > 0:
        tmp = heapq.heappop(heap)
        if tmp[1] == 0:
            heapq.heappush(heap, tmp)
            break
        else:
            tmp[0] += 1
            tmp[1] -= 1
            heapq.heappush(heap, tmp)
        n -= 1
    print(heap)
    total = 0
    for i in range(le):
        total += heap[i][1] * heap[i][1]
    return total


print(solution(4, [4, 3, 3]))
print(solution(1, [2, 1, 2]))
print(solution(10, [3]))