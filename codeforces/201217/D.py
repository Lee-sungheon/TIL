# Busy Robot

for _ in range(int(input())):
    n = int(input())
    commends = [list(map(int, input().split())) for _ in range(n)]
    start_point = 0
    time = commends[0][0] + abs(commends[0][1])
    point = commends[0][1]
    if n == 1:
        result = 1
    else:
        if time <= commends[1][0]:
            result = 1
        else:
            result = 0
        for i in range(1, n):
            if time <= commends[i][0]:
                time = commends[i][0] + abs(point - commends[i][1])
                if i == n-1:
                    result += 1
                else:
                    if time <= commends[i+1][0]:
                        result += 1
                start_point = point
                point = commends[i][1]
            else:
                if start_point >= point:
                    if point < commends[i][1] < start_point:
                        result += 1
                else:
                    if start_point < commends[i][1] < point:
                        result += 1
    print(result)

