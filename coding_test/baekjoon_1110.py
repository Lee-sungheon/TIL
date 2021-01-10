# 더하기 사이클

num = int(input())
cycle = 0
new_num = num

while True:
 
    new_num = int((new_num%10)*10 + (new_num//10 + new_num%10) % 10)
    cycle += 1

    if new_num == num:
        print(cycle)
        break