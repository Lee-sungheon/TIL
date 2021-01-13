# 평균은 넘겠지

n = int(input())
for i in range(n):
    scores = list(map(int, input().split()))
    scores.pop(0)
    avr = sum(scores) / len(scores)
    cnt = 0
    for j in range(len(scores)):
        if scores[j] > avr:
            cnt += 1
    print('%.3f%s' % (round(cnt/len(scores) * 100 ,3), '%'))