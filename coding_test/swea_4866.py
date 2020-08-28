# 괄호 검사

T = int(input())
for tc in range(T):
    words = input()
    stack = []
    for word in words:
        if word in ['[', '(', '{']:
            stack.append(word)
        elif word in [']', ')', '}']:
            if len(stack) == 0:
                print(f'#{tc+1} 0')
                break
            else:
                tmp = stack.pop()
                if tmp == '{' and word == '}':
                    continue
                elif tmp == '(' and word == ')':
                    continue
                elif tmp == '[' and word == ']':
                    continue
                else:
                    print(f'#{tc+1} 0')
                    break
    else:
        if len(stack) == 0:
            print(f'#{tc+1} 1')
        else:
            print(f'#{tc+1} 0')