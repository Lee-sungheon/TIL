# 36진수

N = int(input())
words = [list(map(ord, input())) for _ in range(N)]
num = [0]*36
cnt = 0
K = int(input())
for word in words:
    for i in range(len(word)):
        if 65 <= word[i] <= 90:
            word[i] = word[i] - 55
        num[word[i]] += 1

for i in range(36):
    if num[i] > 0:
        cnt += 1

print(words)
print(num)
