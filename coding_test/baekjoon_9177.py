# 단어 섞기

t = int(input())
for tc in range(t):
    s = list(map(str, input().split()))
    s[0] = list(s[0])
    s[1] = list(s[1])
    for i in range(len(s[2])):
        if s[0] and s[0][0] == s[2][i]:
            if s[1] and s[1][0] == s[2][i]:
                if len(s[0]) < len(s[1]):
                    del s[1][0]
            else:
                del s[0][0]
        elif s[1] and s[1][0] == s[2][i]:
            del s[1][0]
        else:
            print('Data set {}: no' .format(tc+1))
            break
    else:
        print('Data set {}: yes' .format(tc+1))