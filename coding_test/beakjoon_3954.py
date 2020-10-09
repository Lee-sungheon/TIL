# Brainfuck 인터프리터

T = int(input())
for tc in range(T):
    m, c, i = map(int, input().split())
    brain = list(input())
    pro_input = list(input())
    pointer = 0
    brain_li = [0] * c
    idx = idx2 = cnt = 0
    stack = []
    stack2 = []
    while idx < c:
        if brain[idx] == '+':
            brain_li[pointer] += 1
        elif brain[idx] == '-':
            brain_li[pointer] -= 1
        elif brain[idx] == '<':
            pointer -= 1
        elif brain[idx] == '>':
            pointer += 1
        elif brain[idx] == ',':
            if idx2 < i:
                brain_li[pointer] = ord(pro_input[idx2])
                idx2 += 1
            else:
                brain_li[pointer] = 255
        elif brain[idx] == '[':
            stack.append(idx)
            if brain_li[pointer] == 0:
                idx = stack2.pop() - 1
        elif brain[idx] == ']':
            if brain_li[pointer] != 0:
                stack2.append(idx)
                idx = stack.pop() - 1
            else:
                stack.pop()
        idx += 1
        cnt += 1
        if cnt > 50000:
            print("Loops")
            break
    else:
        print('Terminates')