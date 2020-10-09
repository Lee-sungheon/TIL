# 색종이 붙이기
def search(r, c):
    for i in range(10):
        for j in range(10):
            if paper[i][j] == 1:
                size = find_size(r, c)



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
result = -1
search()