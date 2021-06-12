# 키로거
from collections import deque

T = int(input())
for tc in range(T):
    words = list(input())
    li = deque()
    idx = 0
    for word in words:
        if word == '<':
            if idx > 0:
                idx -= 1
        elif word == '>':
            if idx < len(li):
                idx += 1
        elif word == '-':
            if len(li) > idx > 0 and len(li) > 0:
                del li[idx-1]
                idx -= 1
            elif idx >= len(li) > 0:
                del li[len(li)-1]
                idx -= 1
        else:
            li.insert(idx, word)
            idx += 1
    print(''.join(list(li)))
