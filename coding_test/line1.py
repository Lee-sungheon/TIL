def solution(table, languages, preference):
    result = [0] * 5
    languages_name = []
    answer = []
    for k in range(5):
        tmp = table[k].split()
        languages_name.append(tmp[0])
        for i in range(1, 6):
            for j in range(len(languages)):
                if languages[j] == tmp[i]:
                    result[k] += (6-i)*preference[j]
    max_val = max(result)
    for i in range(5):
        if result[i] == max_val:
            answer.append(i)
    for i in range(len(answer)):
        answer[i] = languages_name[answer[i]]
    answer.sort()
    return answer[0]


solution(["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"],
         ["PYTHON", "C++", "SQL"], [7, 5, 5])

solution(["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"],
         ["JAVA", "JAVASCRIPT"], [7, 5])