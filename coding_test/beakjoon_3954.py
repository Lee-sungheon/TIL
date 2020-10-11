# Brainfuck 인터프리터

T = int(input())
for _ in range(T):
    m, c, i = map(int, input().split())
    brain = list(input())
    pro_input = list(map(ord, input())) + [255]
    pair = {}
    tmp_stack = []
    for j in range(c):
        if brain[j] == '[':
            tmp_stack.append(j)
        elif brain[j] == ']':
            x = tmp_stack.pop()
            pair[x] = j
            pair[j] = x
    brain_li = [0] * m
    pointer = idx = idx2 = cnt = 0
    stack = []
    while idx < c:
        if brain[idx] == '+':
            brain_li[pointer] = (brain_li[pointer] + 1) % 256
        elif brain[idx] == '-':
            brain_li[pointer] = (brain_li[pointer] - 1) % 256
        elif brain[idx] == '<':
            pointer = (pointer - 1) % m
        elif brain[idx] == '>':
            pointer = (pointer + 1) % m
        elif brain[idx] == ',':
            brain_li[pointer] = pro_input[idx2]
            if idx2 < i:
                idx2 += 1
        elif brain[idx] == '[':
            if brain_li[pointer] == 0:
                idx = pair[idx]
            else:
                stack.append(idx)
        elif brain[idx] == ']':
            if brain_li[pointer] != 0:
                idx = pair[idx]
            else:
                stack.pop()
        idx += 1
        cnt += 1
        if cnt >= 44000000:  # 50000000
            print(f"Loops {stack[0]} {pair[stack[0]]}")
            break
    else:
        print('Terminates')