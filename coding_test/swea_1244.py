# 최대 상금
def dfs(depth):
    global result
    total = int(''.join(num))
    visited.append([depth, total])
    if depth == change:
        if result <= total:
            result = total
        return
    for i in range(len(num)):
        for j in range(i+1, len(num)):
            num[i], num[j] = num[j], num[i]
            if [depth+1, int(''.join(num))] not in visited:
                dfs(depth+1)
            num[i], num[j] = num[j], num[i]


def same():
    for i in range(10):
        if num.count(str(i)) > 1:
            return True
            break
    return False


T = int(input())
for tc in range(T):
    num, change = map(int, input().split())
    num = list(str(num))
    N = len(num)
    result = 0
    if change >= N-1:
        i = cnt = idx = 0
        while i < N:
            max_num = 0
            for j in range(i, N):
                if max_num < int(num[j]):
                    max_num = int(num[j])
                    idx = j
            if max_num != int(num[i]):
                num[idx], num[i] = num[i], num[idx]
                cnt += 1
            i += 1
        if (change - cnt) % 2 and not same():
            num[-1], num[-2] = num[-2], num[-1]
        result = int(''.join(num))
    else:
        visited = []
        dfs(0)
    print('#{} {}' .format(tc+1, result))

