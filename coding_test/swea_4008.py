# 숫자 만들기
def dfs(dep, total):
    global max_val, min_val
    if dep == N:
        if max_val < total:
            max_val = total
        if min_val > total:
            min_val = total
        return
    for i in range(4):
        if operator[i] > 0:
            operator[i] -= 1
            if i == 0:
                dfs(dep+1, total + number[dep])
            elif i == 1:
                dfs(dep+1, total - number[dep])
            elif i == 2:
                dfs(dep+1, total * number[dep])
            else:
                if total < 0 and total % number[dep]:
                    dfs(dep + 1, total // number[dep] + 1)
                else:
                    dfs(dep + 1, total // number[dep])
            operator[i] += 1


T = int(input())
for tc in range(T):
    N = int(input())
    operator = list(map(int, input().split()))
    number = list(map(int, input().split()))
    min_val = 100000000
    max_val = -100000000
    dfs(1, number[0])
    print('#{} {}' .format(tc+1, max_val-min_val))