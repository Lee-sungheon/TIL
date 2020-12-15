# Unique Number
def dfs(x, s, i):
    global n, result
    if x == n:
        if int(s) < result:
            result = int(s)
        return
    if i > 8:
        return
    dfs(x + num[i], s + str(num[i]), i+1)
    dfs(x, s, i+1)


for _ in range(int(input())):
    n = int(input())
    num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    result = 10000000000
    if n > 45:
        print(-1)
    else:
        dfs(0, '', 0)
        if result == 10000000000:
            print(-1)
        else:
            print(result)
