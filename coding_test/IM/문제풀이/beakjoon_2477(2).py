# 참외밭
# 배열 index 이용
import sys
sys.stdin = open('input1.txt')

N = int(input())
distance = [list(map(int, input().split()))[1] for _ in range(6)]
idx = distance.index(max(distance))
idx2 = distance.index(max(distance[idx-1], distance[(idx+1) % 6]))
total_area = distance[idx]*distance[idx2]
space_area = distance[(idx+3) % 6]*distance[(idx2+3) % 6]
print(N * (total_area - space_area))
