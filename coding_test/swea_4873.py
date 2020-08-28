# 반복문자 지우기
def delete(words):
    tmp = ''
    for i in range(len(words) - 1):
        if words[i+1] == words[i]:
            words.pop(i+1)
            words.pop(i)
            return delete(words)
    else:
        return words

T = int(input())
for tc in range(T):
    words = list(input())
    delete(words)
    print(f'#{tc+1} {len(words)}')