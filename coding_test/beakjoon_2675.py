# 문자열 반복

T = int(input())
for i in range(T):
    N, words = input().split()
    result = ''
    for word in words:
        for j in range(int(N)):
            result += word

    print(result)