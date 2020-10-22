# 특이한 자석
def rotation(idx, way):
    if way == 1:
        magnets[idx] = [magnets[idx][7]] + magnets[idx][:7]
    else:
        magnets[idx] = magnets[idx][1:] + [magnets[idx][0]]
    if 0 <= idx-1 <= 2 and is_sn[idx-1]:
        is_sn[idx-1] = 0
        rotation(idx-1, -way)
    if 0 <= idx+1 <= 3 and is_sn[idx]:
        is_sn[idx] = 0
        rotation(idx+1, -way)


T = int(input())
for tc in range(T):
    K = int(input())
    magnets = [list(map(int, input().split())) for _ in range(4)]
    rotations = [list(map(int, input().split())) for _ in range(K)]
    result = 0
    for i in range(K):
        idx = rotations[i][0] - 1
        is_sn = [0]*3
        for j in range(3):
            if magnets[j][2] != magnets[j+1][6]:
                is_sn[j] = 1
        rotation(idx, rotations[i][1])
    for i in range(4):
        if magnets[i][0] == 1:
            result += 2**i
    print(f'#{tc+1} {result}')