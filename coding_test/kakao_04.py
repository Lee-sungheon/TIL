def solution(new_id):
    new_id = list(new_id.lower())
    delete = []
    # 2단계
    for i in range(len(new_id)):
        if 'a' <= new_id[i] <= 'z':
            continue
        if '0' <= new_id[i] <= '9':
            continue
        if new_id[i] == '-' or new_id[i] == '_' or new_id[i] == '.':
            continue
        delete.append(i)
    for i in range(len(delete)-1, -1, -1):
        new_id.pop(delete[i])
    # 3단계
    cnt = 0
    delete = []
    for i in range(len(new_id)):
        if new_id[i] == '.':
            cnt += 1
        else:
            cnt = 0
        if cnt >= 2:
            delete.append(i)
    for i in range(len(delete)-1, -1, -1):
        new_id.pop(delete[i])
    # 4단계
    while True:
        if new_id[0] == '.':
            new_id.pop(0)
        if len(new_id) >= 1 and new_id[-1] == '.':
            new_id.pop(len(new_id) - 1)
        if len(new_id) < 1 or (new_id[0] != '.' and new_id[-1] != '.'):
            break
    # 5단계
    if len(new_id) == 0:
        new_id.append('a')
    # 6단계
    if len(new_id) >= 16:
        for i in range(len(new_id)-1, 14, -1):
            new_id.pop(i)
    while True:
        if new_id[-1] == '.':
            new_id.pop(len(new_id) - 1)
        else:
            break
    # 7단계
    if len(new_id) == 1:
        new_id += new_id[0] * 2
    elif len(new_id) == 2:
        new_id += new_id[1]

    answer = ''.join(new_id)
    return answer


print(solution('...!@BaT#*..y.abcdefghijklm'))
print(solution('=.='))