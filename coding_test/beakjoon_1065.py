# 한수

number = int(input())

cnt = 0

if number < 100:
    cnt += number

else:
    cnt += 99
    for i in range(100, number+1):
        a = i % 10
        b = i // 10 % 10
        c = i // 100
        if b-a == c-b:
            cnt += 1

print(cnt)