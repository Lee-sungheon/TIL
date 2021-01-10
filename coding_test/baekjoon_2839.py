n = int(input())

total = result = 0
five = n // 5 + 1
three = n // 3 + 1

for i in range(five, -1, -1):
    for j in range(three, -1, -1):
        if n == i*5 + j*3:
            result = i+j
            break
    if result != 0:
        break

else:
    result = -1

print(result)