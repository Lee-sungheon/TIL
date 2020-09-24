# 참외밭
# direction 이용
import sys
sys.stdin = open('input1.txt')

N = int(input())
distance = [list(map(int, input().split())) for _ in range(6)]
# direction 방향에 따른 카운트
cnt_li = [0] * 5
for i in range(6):
    cnt_li[distance[i][0]] += 1
# 카운트 결과에 따른 direction을 인덱스 배열에 저장
idx = []    # 한 방향에 두 변
idx2 = []   # 한 방향에 한 변
for i in range(1, 5):
    if cnt_li[i] == 2:
        idx.append(i)
    else:
        idx2.append(i)
# 한 방향에 한 변일 때 최대 면적이 나오므로 이 떄의 깊이, 너비 구하기
max_width = max_height = 0
for i in range(6):
    if distance[i][0] == idx2[0]:
        max_width = distance[i][1]
    elif distance[i][0] == idx2[1]:
        max_height = distance[i][1]
# SPACE AREA 를 찾기 위해 각 변의 양 옆의 변이 큰 사각형의 너비, 높이가 되는 인덱스를 찾기
space_width = space_height = 0
for i in range(6):
    if distance[i][0] == idx[0]:
        if distance[(i-1)][1] + distance[(i+1) % 6][1] == max_height:
            space_width = distance[i][1]
    elif distance[i][0] == idx[1]:
        if distance[(i-1)][1] + distance[(i+1) % 6][1] == max_width:
            space_height = distance[i][1]
print((max_width*max_height - space_height*space_width)*N)
