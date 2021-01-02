# 6174 (문자열)

t = int(input())
for _ in range(t):
    n = list(input())
    cnt = 0
    if ''.join(n) == '6174':
        print(0)
    else:
        while True:
            cnt += 1
            a = sorted(n)
            b = sorted(n, reverse=True)
            result = int(''.join(b)) - int(''.join(a))
            if result == 6174:
                break
            n = list(str(result))
            if len(n) < 4:
                for _ in range(4-len(n)):
                    n.insert(0, '0')
        print(cnt)
