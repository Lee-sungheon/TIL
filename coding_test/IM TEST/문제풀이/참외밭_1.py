# 참외밭

import sys
sys.stdin = open('input1.txt')

N = int(input())
distance = [list(map(int, input().split()))[1] for _ in range(6)]
# 큰 사각형의 가장 긴 변의 인덱스 구하기
idx1 = distance.index(max(distance))
# 1번의 변에서 양 옆의 변을 확인 후 큰 사각형의 나머지 변 인덱스 구하기
idx2 = distance.index(max(distance[idx1-1], distance[(idx1+1) % 6]))
# 1, 2 번에서 구한 변에서 반시계 방향으로 3만큼 이동해서 빼줘야 하는 사각형의 변을 구하기
total_area = distance[idx1] * distance[idx2]
space_area = distance[(idx1+3) % 6] * distance[(idx2+3) % 6]
# 답 = (큰 사각형 - 작은 사각형) * N
print((total_area - space_area) * N)