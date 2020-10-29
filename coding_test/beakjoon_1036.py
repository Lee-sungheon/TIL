# 36진수

N = int(input())
words = [list(input()) for _ in range(N)]
num = [[0, i] for i in range(36)]
total = 0
K = int(input())
for word in words:
    for i in range(len(word)):
        if 65 <= ord(word[i]) <= 90:
            word[i] = ord(word[i]) - 55
        else:
            word[i] = ord(word[i]) - 48
        num[word[i]][0] += (35 - word[i]) * 36 ** (len(word)-i-1)
num.sort(reverse=True)
print(num)
num = [row[1] for row in num][0:K]
for word in words:
    for i in range(len(word)):
        if word[i] in num:
            word[i] = 35
        total += word[i] * 36 ** (len(word)-i-1)
answer = ''
print(total)
while total > 0:
    mok = total // 36
    na = total % 36
    total = mok
    if 10 <= na <= 35:
        na = chr(na+55)
    answer = str(na) + answer
if answer:
    print(answer)
else:
    print(0)