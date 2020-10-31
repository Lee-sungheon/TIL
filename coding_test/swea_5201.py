# 컨테이너 운반

T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    w = list(map(int, input().split()))
    t = list(map(int, input().split()))
    w.sort(reverse=True)
    t.sort(reverse=True)
    total = 0
    for i in range(M):
        for j in range(len(w)):
            if t[i] >= w[j]:
                total += w[j]
                del w[j]
                break
    print('#{} {}' .format(tc+1, total))