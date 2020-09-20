# 수 이어가기

N = int(input())
max_num = 0
max_list = []
for i in range(N, 0, -1):
    tmp = [N, i]
    while tmp[-1] >= 0:
        tmp.append(tmp[-2] - tmp[-1])
    if max_num < len(tmp) - 1:
        max_num = len(tmp) - 1
        max_list = tmp
max_list.pop()
print(max_num)
print(*max_list)
