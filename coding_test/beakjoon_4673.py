# 셀프 넘버

non_self_num = set()

for i in range(1, 10000):
    total = i
    for num in str(i):
        total += int(num)
    non_self_num.add(total)

for i in range(1, 10000):
    if i not in non_self_num:
        print(i)