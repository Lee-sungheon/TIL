# 부분 문자열 + 같은 알파벳 두 번 이상 X

def solution(s):
    result = []
    answer = 0
    for i in range(len(s)):
        for j in range(i, len(s)+1):
            result.append(s[i:j])
    result = list(set(result))[1:]
    for word in result:
        for alpha in word:
            if word.count(alpha) > 1:
                break
        else:
            answer += 1
    return answer


print(solution("abac"))