def solution(n, k, cmd):
    answer = ''
    stack = []
    dic = {}
    idx = k
    for i in range(n):
        dic[i] = i
    for c in cmd:
        if c[0] == "D":
            idx += int(c[2])
            tmp = list(dic.keys())
            k = tmp[idx]
        elif c[0] == "U":
            idx -= int(c[2])
            tmp = list(dic.keys())
            k = tmp[idx]
        elif c[0] == "C":
            stack.append(dic.pop(k))
            tmp = list(dic.keys())
            if idx >= len(tmp):
                idx -= 1
            k = tmp[idx]
        elif c[0] == "Z":
            x = stack.pop()
            dic = {}
            for i in range(n):
                if not i in stack:
                    dic[i] = i
            if x < idx:
                idx += 1
    for i in range(n):
        if i in stack:
            answer += 'X'
        else:
            answer += 'O'
    return answer

print(solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]))
print(solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]))