# 그룹 단어 체커
N = int(input())
cnt = 0
for _ in range(N):
    words = list(input())
    tmp = 1
    for i in range(1, len(words)):
        if words[i] != words[i-1]:
            tmp += 1
    if len(set(words)) == tmp:
        cnt += 1
print(cnt)