# 단어 섞기

t = int(input())
for tc in range(t):
    s = list(map(str, input().split()))
    a = list(s[0])
    b = list(s[1])
    c = list(s[2])
    memo = [[False]*len(b) for _ in range(len(a))]
    memo[0][0] = True
    for i in range(1, len(a)):
        if a[i-1] == c[i-1]:
            memo[i][0] = memo[i-1][0]
        else:
            memo[i][0] = False
    for i in range(1, len(b)):
        if b[i-1] == c[i-1]:
            memo[0][i] = memo[0][i-1]
        else:
            memo[0][i] = False
    for i in range(1, len(a)):
        for j in range(1, len(b)):
            cura, curb, curc = a[i-1], b[j-1], c[i+j-1]
            if cura != curc and curb != curc:
                memo[i][j] = False
            elif cura == curc and curb != curc:
                memo[i][j] = memo[i-1][j]
            elif cura != curc and curb == curc:
                memo[i][j] = memo[i][j-1]
            else:
                memo[i][j] = memo[i-1][j] | memo[i][j-1]
    if memo[-1].count(True) > 0:
        print("Data set {}: yes" .format(tc+1))
    else:
        print("Data set {}: no".format(tc + 1))

