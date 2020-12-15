# Favorite Sequence

from collections import deque

for _ in range(int(input())):
    n = int(input())
    b = deque(map(int, input().split()))
    result = []
    for i in range(n):
        if i % 2 == 0:
            result.append(b.popleft())
        else:
            result.append(b.pop())
    print(*result)