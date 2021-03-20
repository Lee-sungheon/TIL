def solution(inp_str):
    answer = []
    n = len(inp_str)
    cnt = [0]*5
    special = ['~', '!', '@', '#', '$', '%', '^', '&', '*']
    word = inp_str[0]
    same_cnt = 1
    if n > 15 or n < 8:
        answer.append(1)
    for i in range(n):
        if 'A' <= inp_str[i] <= 'Z':
            cnt[0] += 1
        elif 'a' <= inp_str[i] <= 'z':
            cnt[1] += 1
        elif '0' <= inp_str[i] <= '9':
            cnt[2] += 1
        elif inp_str[i] in special:
            cnt[3] += 1
        else:
            cnt[4] += 1

        if i != 0:
            if same_cnt >= 4:
                continue
            if word == inp_str[i]:
                same_cnt += 1
            else:
                same_cnt = 1
            word = inp_str[i]

    if cnt[4] > 0:
        answer.append(2)
    if cnt[0:4].count(0) > 1:
        answer.append(3)

    if same_cnt >= 4:
        answer.append(4)

    same = list(set(list(inp_str)))
    for s in same:
        if inp_str.count(s) >= 5:
            answer.append(5)

    if len(answer) == 0:
        answer.append(0)

    return answer

print(solution("AaTa+!12-3"))
print(solution("aaaaZZZZ)"))
print(solution("CaCbCgCdC888834A"))
print(solution("UUUUU"))
print(solution("ZzZz9Z824"))