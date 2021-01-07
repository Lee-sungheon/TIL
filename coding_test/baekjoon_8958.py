# OX 퀴즈

n = int(input())
for i in range(n):
    score = 0
    ox_quiz = input()
    cnt = 0
    for ox in ox_quiz:
        if ox == 'O':
            cnt += 1
            score += cnt
        else:
            cnt = 0
    print(score)