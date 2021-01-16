# 일곱 난쟁이
def seven(n, k, sum):
    if k == 7 and sum == 100:
        idx = 0
        for i in range(9):
            if visited[i]:
                seven_nanjangs[idx] = nanjangs[i]
                idx += 1
        seven_nanjangs.sort()
        return
    if n >= 9:
        return
    visited[n] = 1
    seven(n+1, k+1, sum + nanjangs[n])
    visited[n] = 0
    seven(n+1, k, sum)


nanjangs = [int(input()) for _ in range(9)]
seven_nanjangs = [0]*7
visited = [0] * 9
seven(0, 0, 0)
for i in range(7):
    print(seven_nanjangs[i])
