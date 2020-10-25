# 00000010001101
# 0000000111100000011000000111100110000110000111100111100111111001100111
arr = list(map(int, input()))
result = []
for i in range(len(arr)//7):
    total = 0
    tmp_li = arr[7*i:7*(i+1)]
    for j in range(7):
        if tmp_li[6-j] == 1:
            total += (1 << j)
    result.append(total)
print(*result)