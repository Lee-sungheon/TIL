# 종이자르기
W, H = map(int, input().split())
N = int(input())
width, height = [0, W], [0, H]
for _ in range(N):
    num, idx = map(int, input().split())
    if num == 0:
        height.append(idx)
    else:
        width.append(idx)
height.sort()
width.sort()
max_height = max_width = 0
for i in range(1, len(height)):
    temp = height[i] - height[i-1]
    if temp > max_height:
        max_height = temp
for i in range(1, len(width)):
    temp = width[i] - width[i - 1]
    if temp > max_width:
        max_width = temp
print(max_height*max_width)
