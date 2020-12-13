# [모의 SW 역량테스트] 활주로 건설
import copy

T = int(input())
for tc in range(T):
    N, X = map(int, input().split())
    airstrip = [list(map(int, input().split())) for _ in range(N)]
    airstrip2 = copy.deepcopy(airstrip)
    visited = [[False]*N for _ in range(N)]
    visited2 = [[False]*N for _ in range(N)]
    result = 0
    # 행 왼 -> 오
    a = set()
    for i in range(N):
        for j in range(N-1):
            isLoop = False
            if 6 > airstrip[i][j] - airstrip[i][j+1] > 1:
                break
            elif airstrip[i][j] - airstrip[i][j+1] == 1:
                val = airstrip[i][j+1]
                for k in range(X):
                    if j+1+k >= N:
                        isLoop = True
                        break
                    elif airstrip[i][j+1+k] != val or visited[i][j+1+k]:
                        isLoop = True
                        break
                    visited[i][j+1+k] = True
                if isLoop:
                    break
        else:
            a.add(i)
    # 행 오 -> 왼
    b = set()
    for i in range(N):
        for j in range(N-1, 0, -1):
            isLoop = False
            if 6 > airstrip[i][j] - airstrip[i][j-1] > 1:
                break
            elif airstrip[i][j] - airstrip[i][j-1] == 1:
                val = airstrip[i][j-1]
                for k in range(X):
                    if j-1-k < 0:
                        isLoop = True
                        break
                    elif airstrip[i][j-1-k] != val or visited[i][j - 1 - k]:
                        isLoop = True
                        break
                    visited[i][j-1-k] = True
                if isLoop:
                    break
        else:
            b.add(i)
    result = len(a & b)
    # 열 위 -> 아래
    a = set()
    for i in range(N):
        for j in range(N-1):
            isLoop = False
            if 6 > airstrip2[j][i] - airstrip2[j+1][i] > 1:
                break
            elif airstrip2[j][i] - airstrip2[j+1][i] == 1:
                val = airstrip2[j+1][i]
                for k in range(X):
                    if j+1+k >= N:
                        isLoop = True
                        break
                    elif airstrip2[j+1+k][i] != val or visited2[j+1+k][i]:
                        isLoop = True
                        break
                    visited2[j+1+k][i] = True
                if isLoop:
                    break
        else:
            a.add(i)
    # 열 아래 -> 위
    b = set()
    for i in range(N):
        for j in range(N-1, 0, -1):
            isLoop = False
            if 6 > airstrip2[j][i] - airstrip2[j-1][i] > 1:
                break
            elif airstrip2[j][i] - airstrip2[j-1][i] == 1:
                val = airstrip2[j-1][i]
                for k in range(X):
                    if j-1-k < 0:
                        isLoop = True
                        break
                    elif airstrip2[j-1-k][i] != val or visited2[j-1-k][i]:
                        isLoop = True
                        break
                    visited2[j-1-k][i] = True
                if isLoop:
                    break
        else:
            b.add(i)
    result += len(a & b)
    print("#{} {}" .format(tc+1, result))
