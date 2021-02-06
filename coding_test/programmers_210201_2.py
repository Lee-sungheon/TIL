# 가장 긴 팰린드롬

def solution(s):
    answer = 0
    for i in range(len(s), 0, -1):
        for j in range(0,len(s)-i+1):
            x = s[j:j+i]
            if x == x[::-1]:
                return len(s[j:j+i])
    return answer