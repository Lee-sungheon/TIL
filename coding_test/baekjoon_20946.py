# 합성인수분해

N = int(input())
array = []
for i in range(2, int(N ** 0.5) + 1):
    while(N > 1):
        if(N % i == 0):
            N //= i
            array.append(i)
        else:
            break
if N > 1:
    array.append(N)
print(array)

result = []
array_len = len(array)
if array_len == 0 or array_len == 1:
    print(-1)
else:
    for i in range(array_len):
        if i % 2 == 0:
            if i == array_len-1:
                result[-1] = result[-1] * array[i]
            else:
                result.append(array[i])
        else:
            result[-1] = result[-1]*array[i]
print(*result)
