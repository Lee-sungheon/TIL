# 참외밭

N = int(input())
distance = [list(map(int, input().split())) for _ in range(6)]
cnt_li = [0] * 5
for i in range(6):
    cnt_li[distance[i][0]] += 1

idx = []    # 두 변 이상
idx2 = []   # 각 변
for i in range(1, 5):
    if cnt_li[i] == 2:
        idx.append(i)
    else:
        idx2.append(i)

max_width = max_height = 0
for i in range(6):
    if distance[i][0] == idx2[0]:
        max_width = distance[i][1]
    elif distance[i][0] == idx2[1]:
        max_height = distance[i][1]

space_width = space_height = 0
for i in range(6):
    if distance[i][0] == idx[0]:
        if distance[(i-1)%6][1] + distance[(i+1)%6][1] == max_height:
            space_width = distance[i][1]
    elif distance[i][0] == idx[1]:
        if distance[(i-1)%6][1] + distance[(i+1)%6][1] == max_width:
            space_height = distance[i][1]
print((max_width*max_height - space_height*space_width)*N)