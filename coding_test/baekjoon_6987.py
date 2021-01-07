# 월드컵
import sys
sys.setrecursionlimit(10**8)


def dfs(cnt):
    global result
    if cnt == 15:
        if win.count(0) == 6 and lose.count(0) == 6 and draw.count(0) == 6:
            result = 1
            return
        else:
            return
    if win[game[cnt][0]] > 0 and lose[game[cnt][1]] > 0:
        win[game[cnt][0]] -= 1
        lose[game[cnt][1]] -= 1
        dfs(cnt + 1)
        win[game[cnt][0]] += 1
        lose[game[cnt][1]] += 1
    if win[game[cnt][1]] > 0 and lose[game[cnt][0]] > 0:
        lose[game[cnt][0]] -= 1
        win[game[cnt][1]] -= 1
        dfs(cnt + 1)
        lose[game[cnt][0]] += 1
        win[game[cnt][1]] += 1
    if draw[game[cnt][0]] > 0 and draw[game[cnt][1]] > 0:
        draw[game[cnt][0]] -= 1
        draw[game[cnt][1]] -= 1
        dfs(cnt + 1)
        draw[game[cnt][0]] += 1
        draw[game[cnt][1]] += 1

answer = []
game = [(0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (1, 2), (1, 3), (1, 4), (1, 5), (2, 3), (2, 4), (2, 5), (3, 4), (3, 5), (4, 5)]
for _ in range(4):
    result = 0
    tmp = list(map(int, input().split()))
    win, lose, draw = [], [], []
    for i in range(18):
        if i % 3 == 0:
            win.append(tmp[i])
        elif i % 3 == 1:
            draw.append(tmp[i])
        else:
            lose.append(tmp[i])
    dfs(0)
    answer.append(result)
print(*answer)