# 종이자르기
import sys
sys.stdin = open('input2.txt')

W, H = map(int, input().split())
N = int(input())

# 너비, 높이를 따로 나누어서 생각하기
width, height = [0, W], [0, H]
for _ in range(N):
    num, idx = map(int, input().split())
    if num == 0:
        height.append(idx)
    else:
        width.append(idx)
# 조각의 길이를 구하기 위해 각 배열을 정렬하기
height.sort()
width.sort()
# max_height / max_width 구해주기
max_height = max_width = 0
for i in range(1, len(height)):
    temp = height[i] - height[i-1]
    if temp > max_height:
        max_height = temp
for i in range(1, len(width)):
    temp = width[i] - width[i-1]
    if temp > max_width:
        max_width = temp
# 답 : (max_height * max_width)!!
print(max_height * max_width)