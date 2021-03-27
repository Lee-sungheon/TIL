# 커피 추출기
from collections import deque
from queue import PriorityQueue


def solution(N, coffee_times):
    answer = []
    coffee_times = deque(coffee_times)
    make_coffee = PriorityQueue()
    for i in range(1, N+1):
        if coffee_times:
            make_coffee.put((coffee_times.popleft(), i))
    order = 1+N
    value = 0
    prev = 0
    while True:
        tmp = make_coffee.get()
        answer.append(tmp[1])
        if prev != tmp[0]:
            value += tmp[0] - prev
        prev = tmp[0]
        if coffee_times:
            make_coffee.put((coffee_times.popleft()+value, order))
            order += 1
        if make_coffee.empty():
            break
    return answer


print(solution(3, [4, 2, 2, 5, 3]))
print(solution(1, [100, 1, 50, 1, 1]))
print(solution(3, [100000, 1, 50, 1, 1]))
print(solution(2, [2, 1, 3, 1, 2]))