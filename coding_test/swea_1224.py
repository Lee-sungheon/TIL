# 계산기 3 - stack

for tc in range(10):
    length = int(input())
    string = input()
    token = []
    cal = []
    stack = []
    icp = isp = 0
    for st in string:
        if st == '*':
            icp = 2
            if icp > isp:
                token.append(st)
            else:
                while True:
                    tmp = token.pop()
                    if tmp == '+' or tmp == '(':
                        token.append(tmp)
                        break
                    cal.append(tmp)
                token.append(st)
            isp = 2
        elif st == '+':
            icp = 1
            if icp > isp:
                token.append(st)
            else:
                while True:
                    tmp = token.pop()
                    if tmp == '(':
                        token.append(tmp)
                        break
                    cal.append(tmp)
                token.append(st)
            isp = 1
        elif st == '(':
            icp = 3
            token.append(st)
            isp = 0
        elif st == ')':
            while True:
                tmp = token.pop()
                if tmp == '(':
                    break
                cal.append(tmp)
        else:
            cal.append(int(st))

    for c in cal:
        if c == '*':
            b = stack.pop()
            a = stack.pop()
            stack.append(a * b)
        elif c == '+':
            b = stack.pop()
            a = stack.pop()
            stack.append(a + b)
        else:
            stack.append(c)
    print(f'#{tc+1} {stack[0]}')
