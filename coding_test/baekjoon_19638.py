# 센티와 마법의 뿅망치
import heapq, sys

input = sys.stdin.readline
N, H, T = map(int, input().split())
giant = []
for _ in range(N):
    heapq.heappush(giant, -int(input()))
for i in range(T):
    if -giant[0] < H:
        print("YES\n{}" .format(i))
        exit(0)
    if -giant[0] == 1:
        break
    tmp = -heapq.heappop(giant)
    tmp = tmp//2
    heapq.heappush(giant, -tmp)
if -giant[0] < H:
    print("YES\n{}" .format(T))
    exit(0)
print("NO\n{}" .format(-giant[0]))
