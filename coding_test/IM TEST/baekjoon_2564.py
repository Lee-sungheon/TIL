# 경비원
N, M = map(int, input().split())
T = int(input())
array = [list(map(int, input().split())) for _ in range(T)]
start_direction, start_distance = map(int, input().split())
min_distance = 0
if start_direction == 1 or start_direction == 2:
    for dire, dis in array:
        if dire == start_direction:
            min_distance += abs(dis - start_distance)
        elif dire == 3:
            if start_direction == 1:
                min_distance += (start_distance + dis)
            else:
                min_distance += (start_distance + M - dis)
        elif dire == 4:
            if start_direction == 1:
                min_distance += (N-start_distance + dis)
            else:
                min_distance += (N - start_distance + M - dis)
        else:
            min_distance += min(start_distance + M + dis, N-start_distance + M + N-dis)
else:
    for dire, dis in array:
        if dire == start_direction:
            min_distance += abs(dis - start_distance)
        elif dire == 1:
            if start_direction == 3:
                min_distance += (start_distance + dis)
            else:
                min_distance += (start_distance + N - dis)
        elif dire == 2:
            if start_direction == 3:
                min_distance += (M-start_distance + dis)
            else:
                min_distance += (M - start_distance + N - dis)
        else:
            min_distance += min(start_distance + N + dis, M-start_distance + N + M-dis)
print(min_distance)
