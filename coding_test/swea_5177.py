# 이진 힙
def heappush(value):
    global heap_count
    heap_count += 1
    heap[heap_count] = value
    cur = heap_count
    parent = cur // 2
    while parent and heap[parent] > heap[cur]:
        heap[parent], heap[cur] = heap[cur], heap[parent]
        cur = parent
        parent = cur // 2


T = int(input())
for tc in range(T):
    N = int(input())
    heap_count = 0
    total = 0
    heap = [0] * (N + 1)
    numbers = list(map(int, input().split()))
    for i in range(N):
        heappush(numbers[i])
    while N > 0:
        N = N//2
        total += heap[N]
    print(f'#{tc+1} {total}')