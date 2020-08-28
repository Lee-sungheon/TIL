# 어디에 단어가 들어갈 수 있을까

T = int(input())

for tc in range(T):
    N, K = map(int, input().split())
    puzzle = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0
    for i in range(N):
        cnt1 = 0
        cnt2 = 0
        for j in range(N):
            if puzzle[i][j] == 1:
                cnt1 += 1
                if cnt1 == K and j == N-1:
                    cnt += 1
                elif cnt1 == K and j < N-1 and puzzle[i][j+1] == 0:
                    cnt += 1
            else:
                cnt1 = 0
            if puzzle[j][i] == 1:
                cnt2 += 1
                if cnt2 == K and j == N-1:
                    cnt += 1
                elif cnt2 == K and j < N-1 and puzzle[j+1][i] == 0:
                    cnt += 1
            else:
                cnt2 = 0
    print(f'#{tc+1} {cnt}')