# 색종이 붙이기

def search(x, cnt):
    global result
    if x == 100:
        for i in range(10):
            if paper[i].count(1) > 0:
                return
        else:
            if cnt < result:
                result = cnt
            return

    if paper[x//10][x % 10] == 1:
        if cnt >= result:
            return

        size = find_size(x//10, x % 10)
        for k in range(size, 0, -1):
            if num[k] > 0:
                num[k] -= 1
                change_paper(x//10, x % 10, k, 0)
                search(x+1, cnt + 1)
                num[k] += 1
                change_paper(x//10, x % 10, k, 1)
    else:
        search(x+1, cnt)


def change_paper(r, c, size, x):
    for i in range(size):
        for j in range(size):
            paper[r+i][c+j] = x
    return


def find_size(r, c):
    size = 1
    for k in range(2, 6):
        for i in range(k):
            for j in range(k):
                if r+i == 10 or c+j == 10 or paper[r+i][c+j] == 0:
                    return size
        else:
            size += 1
    return size


paper = [list(map(int, input().split())) for _ in range(10)]
result = 26
num = [0, 5, 5, 5, 5, 5]
search(0, 0)
if result == 26:
    print(-1)
else:
    print(result)