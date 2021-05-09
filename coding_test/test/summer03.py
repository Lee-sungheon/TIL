from collections import deque

def solution(maps, p, r):
    answer = 0
    length = len(maps)
    for i in range(length):
        for j in range(length):
            kill = 0
            for m in range(i, i+(r//2)):
                for n in range(j-m, j+m):
                    if m < 0 or n < 0 or m >= length or n >= length:
                        continue
                    if n == j-m or n == j+m-1:
                        if maps[m][n] <= p/2:
                            kill += 1
                    else:
                        if maps[m][n] <= p:
                            kill += 1
            for m in range(i-(r//2), i):
                for n in range(j-m, j+m):
                    if m < 0 or n < 0 or m >= length or n >= length:
                        continue
                    if n == j-m or n == j+m-1:
                        if maps[m][n] <= p/2:
                            kill += 1
                    else:
                        if maps[m][n] <= p:
                            kill += 1
            if kill > answer:
                answer = kill
            print(kill)
    return answer

solution([[1, 28, 41, 22, 25, 79, 4], [39, 20, 10, 17, 19, 18, 8], [21, 4, 13, 12, 9, 29, 19], [58, 1, 20, 5, 8, 16, 9], [5, 6, 15, 2, 39, 8, 29],[39, 7, 17, 5, 4, 49, 5], [74, 46, 8, 11, 25, 2, 11]], 19, 6)