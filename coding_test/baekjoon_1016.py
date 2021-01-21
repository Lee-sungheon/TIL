# 제곱 ㄴㄴ수

min, max = map(int, input().split())
array = [0]*1000001

for i in range(2, max):
    if i*i > max:
        break
    start = i*i - min%(i*i)
    if start == i*i:
        start = 0
    for j in range(start, max-min+1, i*i):
        array[j] = 1
result = 0
for i in range(max-min+1):
    if array[i] == 0:
        result += 1
print(result)