# 종이자르기

W, H = map(int, input().split())
N = int(input())
width = [W]
height = [H]
for _ in range(N):
    num, idx = map(int, input().split())
    total = 0
    if num == 0:
        for i in range(len(height)):
            if i > 0:
                idx -= height[i-1]
            total += height[i]
            if height[i] > idx:
                height.insert(i+1, height[i] - idx)
                height[i] = idx
                break
    else:
        for i in range(len(width)):
            if i > 0:
                idx -= width[i - 1]
            total += width[i]
            if width[i] > idx:
                width.insert(i + 1, width[i] - idx)
                width[i] = idx
                break
print(max(height)*max(width))
