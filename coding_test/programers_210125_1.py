def solution(info, query):
    answer = []
    coding = {'cpp': {'backend': {'junior': {'chicken': [], 'pizza': []}, 'senior': {'chicken': [], 'pizza': []}}, 'frontend': {'junior': {'chicken': [], 'pizza': []}, 'senior': {'chicken': [], 'pizza': []}}},
              'java': {'backend': {'junior': {'chicken': [], 'pizza': []}, 'senior': {'chicken': [], 'pizza': []}}, 'frontend': {'junior': {'chicken': [], 'pizza': []}, 'senior': {'chicken': [], 'pizza': []}}},
              'python': {'backend': {'junior': {'chicken': [], 'pizza': []}, 'senior': {'chicken': [], 'pizza': []}}, 'frontend': {'junior': {'chicken': [], 'pizza': []}, 'senior': {'chicken': [], 'pizza': []}}}}

    for i in range(len(info)):
        tmp = info[i].split()
        coding[tmp[0]][tmp[1]][tmp[2]][tmp[3]].append(int(tmp[4]))

    for i in range(len(query)):
        tmp = query[i].split('and')
        score = tmp[3].split()[1]
        for i in range(3):
            tmp[i] = tmp[i].strip()
        tmp2 = tmp[0:3]
        tmp2.append(tmp[3].split()[0])
        result = []
        if tmp2[0] == '-':
            result.append(coding['cpp'])
            result.append(coding['java'])
            result.append(coding['python'])
        else:
            result.append(coding[tmp2[0]])

        x = 0
        for i in range(len(result)):
            if tmp2[1] == '-':
                result.append(result[i]['backend'])
                result.append(result[i]['frontend'])
            else:
                result.append(result[i][tmp2[1]])
            x += 1
        for i in range(x):
           del result[0]

        x = 0
        for i in range(len(result)):
            if tmp2[2] == '-':
                result.append(result[i]['junior'])
                result.append(result[i]['senior'])
            else:
                result.append(result[i][tmp2[2]])
            x += 1
        for i in range(x):
            del result[0]

        x = 0
        for i in range(len(result)):
            if tmp2[3] == '-':
                result.append(result[i]['chicken'])
                result.append(result[i]['pizza'])
            else:
                result.append(result[i][tmp2[3]])
            x += 1
        for i in range(x):
            del result[0]
        cnt = 0
        for i in range(len(result)):
            if result[i]:
                for j in range(len(result[i])):
                    if result[i][j] >= int(score):
                        cnt += 1
        answer.append(cnt)
    return answer

solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"],
         ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"])


