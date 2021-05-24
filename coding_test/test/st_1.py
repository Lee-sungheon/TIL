def solution(S):
    cnt = 0
    S = list(str(int(S)))
    while True:
        print(S)
        if len(S) == 1 and S[len(S) - 1] == '0':
            break
        if S[len(S) - 1] == '0':
            S.pop()
        else:
            S[len(S) - 1] = '0'
        cnt += 1
    return cnt

print(solution('011100'))