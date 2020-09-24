# 참외밭
# 배열 index 이용

N = int(input())
distance = [list(map(int, input().split()))[1] for _ in range(6)]
idx = distance.index(max(distance))
idx2 = distance.index(max(distance[idx-1], distance[(idx+1) % 6]))
print(N*(distance[idx]*distance[idx2] - distance[(idx+3) % 6]*distance[(idx2+3) % 6]))
