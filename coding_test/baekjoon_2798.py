# 블랙잭 (브루트 포스)
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
cards = list(map(int, input().split()))
result = 0
for i in range(n):
    for j in range(n):
        for k in range(n):
            if i != j and j != k and i != k and cards[i] + cards[j] + cards[k] <= m:
                result = max(result, cards[i] + cards[j] + cards[k])
print(result)