# [모의 SW 역량테스트] 원자 소멸 시뮬레이션

T = int(input())
for tc in range(T):
    N = int(input())
    atomics = [list(map(int, input().split())) for _ in range(N)]
    delta = {0: (0, 1), 1: (0, -1), 2: (-1, 0), 3: (1, 0)}
    result = 0
    for i in range(N):
        atomics[i][0] *= 2
        atomics[i][1] *= 2

    for _ in range(4002):
        for i in range(len(atomics)):
            dx, dy = delta[atomics[i][2]]
            atomics[i][0] += dx
            atomics[i][1] += dy

        idx = set()
        atomics.sort()

        delete = []
        for i in range(len(atomics)):
            if atomics[i][0] > 2000 or atomics[i][0] < -2000 or atomics[i][1] > 2000 or atomics[i][0] < -2000:
                delete.append(i)

        for i in range(len(delete) - 1, -1, -1):
            del atomics[delete[i]]

        for i in range(1, len(atomics)):
            if atomics[i][0] == atomics[i - 1][0] and atomics[i][1] == atomics[i - 1][1]:
                idx.add(i)
                idx.add(i - 1)
        idx = list(idx)
        idx.sort()

        for i in range(len(idx) - 1, -1, -1):
            result += atomics[idx[i]][3]
            del atomics[idx[i]]

        if len(atomics) <= 1:
            break
    print("#{} {}".format(tc + 1, result))