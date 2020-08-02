# 나머지

numbers = []
for i in range(10):
    numbers.append(int(input()))
    numbers[i] = numbers[i] % 42

print(len(set(numbers)))