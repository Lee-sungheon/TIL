def solution(program, flag_rules, commands):
    # argument의 type 확인을 위한 함수를 정의합니다.
    def confirm_type(argument):
        argument_type = 'FALSE'
        # NUMBER 및 STRING은 서로 섞인 형태이면 안되므로 이를 확인하기 위한 bool을 생성합니다.
        num = string = True
        # 반복문을 돌며 type을 확인합니다.
        for i in range(len(argument)):
            if '0' <= argument[i] <= '9' and num:
                string = False
            elif 'A' <= argument[i] <= 'Z' or 'a' <= argument[i] <= 'z' and string:
                num = False
            # NUMBER와 STRING 형태가 모두 만족을 못할 때 반복문을 빠져나갑니다.
            elif not num and not string:
                break
            # 어느 조건에도 해당하지 않을 때 반복문을 빠져나갑니다.
            else:
                break
        # 반복문을 다 돌고 빠져나왔을 시, type을 확인해줍니다.
        else:
            if num:
                argument_type = 'NUMBER'
            elif string:
                argument_type = 'STRING'
        return argument_type


    answer = []
    # flag_rules를 dictionary 형태로 저장합니다.
    flag_rules_dic = {}
    for flag_rule in flag_rules:
        tmp = flag_rule.split()
        # 별칭이 있을 때는 배열의 길이가 3이므로 이를 구분해서 dic에 저장해줍니다.
        if len(tmp) == 2:
            flag_rules_dic[tmp[0]] = tmp[1]
        if len(tmp) > 2:
            flag_rules_dic[tmp[0]] = tmp[2]
    # flag와 command 비교를 위해 flag 목록을 리스트 형태로 저장합니다.
    flag_keys = flag_rules_dic.keys()
    flag_values = list(flag_rules_dic.values())

    for command in commands:
        # 코맨드를 띄워쓰기를 기점으로 split하여 배열형태로 저장합니다.
        confirm_command = command.split()
        # 프로그램명이 다르다면 False를 answer에 저장하고 다음 코맨드를 확인합니다.
        if confirm_command[0] != program:
            answer.append(False)
            continue
        # 프로그램명이 같다면 command가 flag rule을 지키는지 확인합니다.
        idx = 1
        n = len(confirm_command)
        is_flag = True
        flag_list = []
        flag_name = ''
        while idx < n and is_flag:
            # command의 flag가 flag 목록에 있다면 해당하는 type을 확인해주고 type이 맞는지 확인합니다.
            # ALIAS를 추가하여 바뀐 알고리즘입니다.
            if confirm_command[idx] in flag_keys:
                flag_list.append(confirm_command[idx])
                if flag_rules_dic[confirm_command[idx]][0] != '-':
                    flag_argument_type = flag_rules_dic[confirm_command[idx]]

                else:
                    flag_name = flag_rules_dic[confirm_command[idx]]
                    # ALIAS의 ALIAS가 존재할 때 FALSE 처리입니다.
                    if flag_rules_dic[flag_rules_dic[confirm_command[idx]]][0] == '-':
                        is_flag = False
                        break
                    # 하나의 flag가 2개 이상의 ALIAS를 가질 때 FALSE 처리입니다.
                    elif flag_values.count(flag_name) > 1:
                        is_flag = False
                        break
                    else:
                        flag_argument_type = flag_rules_dic[flag_rules_dic[confirm_command[idx]]]
                # file_name1, 2를 동시에 입력했을 때 FALSE 처리입니다.
                if flag_name in flag_list:
                    is_flag = False
                    break
                idx += 1
                # type이 NULL 값이 아닐 때 처리를 해줍니다.
                if flag_argument_type != 'NULL':
                    # idx가 배열을 벗어나면 flag에 해당하는 argument가 없는 것이므로 False를 리턴합니다.
                    if idx >= n:
                        is_flag = False
                        break
                    # 반복문을 돌며 다음 flag가 나올 때까지 argument들을 확인합니다.
                    arguments = []
                    while idx < n and confirm_command[idx][0] != '-':
                        arguments.append(confirm_command[idx])
                        idx += 1
                    # 만약 type이 NUMBER, STRING이라면 argument는 하나여야만 하고, 이를 만족할 때 type 검사를 해줍니다.
                    if flag_argument_type == "NUMBER" or flag_argument_type == "STRING":
                        if len(arguments) == 1:
                            if confirm_type(arguments[0]) != flag_argument_type:
                                is_flag = False
                                break
                        else:
                            is_flag = False
                            break
                    # 만약 type이 NUMBERS라면 모든 argument는 NUMBER 형태여야 합니다.
                    elif flag_argument_type == "NUMBERS":
                        for argument in arguments:
                            if confirm_type(argument) != "NUMBER":
                                is_flag = False
                                break
                    # 만약 type이 STRINGS라면 모든 argument는 STRING 형태여야 합니다.
                    elif flag_argument_type == "STRINGS":
                        for argument in arguments:
                            if confirm_type(argument) != "STRING":
                                is_flag = False
                                break
                # 이 흐름대로라면 NULL 값일 때는 따로 처리할 필요가 없습니다.
            # command의 flag가 flag 목록에 없다면 False를 반환합니다.
            else:
                is_flag = False
                break
        # 반복문이 끝나고 is_flag가 true라면 True, false라면 False를 answer에 넣어줍니다.
        if is_flag:
            answer.append(True)
        else:
            answer.append(False)
    return answer

# 읽기 편한, 확장 가능한, 의도를 설명하는 주석, 테스트가 용이한


print(solution('line', ["-s STRING", "-num NUMBER", "-e NULL", "-n ALIAS -num", "-nm ALIAS -num", "-nmn ALIAS -n"], ["line -n 100 -s hi -e", "line -n 100 -e -num 150"]))
print(solution('bank', ["-send STRING", "-a ALIAS -amount", "-amount NUMBERS"], ["bank -send abc -amount 500 200 -a 400", "bank -send abc -a hey"]))

# print(solution('line', ["-s STRINGS", "-n NUMBERS", "-e NULL"], ["line -n 100 102 -s hi -e", "line -n id pwd -n 100"]))
# print(solution('trip', ["-days NUMBERS", "-dest STRING"], ["trip -days 15 10 -dest Seoul Paris", "trip -days 10 -dest Seoul"]))
#
# print(solution('line', ["-s STRING", "-n NUMBER", "-e NULL"], ["line -n 100 -s hi -e", "lien -s Bye"]))
# print(solution('line', ["-s STRING", "-n NUMBER", "-e NULL"], ["line -s 123 -n HI", "line fun"]))