# 정사각형

size = list(map(int, input().split()))

rect = list()
for i in range(size[0]):
    rect.append(input())

result = 0
min_size = 0

if size[0] >= size[1]:
    min_size = size[1]
else:
    min_size = size[0]

for i in range(0, min_size):
    for j in range(size[1]):
        for k in range(size[0] - i):
            if j+i < size[1]:
                if rect[k][j] == rect[k][j+i] == rect[k+i][j] == rect[k+i][j+i]:
                    if (i+1)**2 > result:
                        result = (i+1)**2

print(result)

