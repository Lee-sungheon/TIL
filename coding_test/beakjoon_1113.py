# 수영장 만들기
def is_range(r, c):
    if r < 0 or c < 0 or r >= N or c >= M:
        return 0
    return 1


N, M = map(int, input().split())
pool = list(map(int, input().split()) for _ in range(N))
