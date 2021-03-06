# 장훈이의 높은 선반(백트래킹)
def f1(n, g, K, m): # n 고려할 직원번호, g 직원 수, K 선반높이, m n-1번까지 선반높이
    global minV
    if n==g:
        if minV>m-K and m>=K:
            minV = m-K
    elif m>=K and minV <= m-K:
        return
    else:
        f1(n+1, g, K, m) # n번 탑에 참여하지 않음 (이전 직원까지 높이)
        f1(n+1, g, K, m+heights[n]) # n-1까지의 높이 m + H[n] n번 직업의 높이

# def f(n, g, K):    # n 고려할 직원번호, g 직원 수
#     global minV
#     if n==g:    # 모든 직원에 대해 고려
#         s = 0
#         for i in range(g):
#             if A[i]:    # 참여하는 경우
#                 s += hegihts[i] # 키를 더함
#         if K <= s and s-K < minV:   # 키의 합이 선반 이상이고, 차이가 최소이면
#             minV = s-K
#     else:
#         A[n] = 0 # n번 직원 미참여
#         f(n+1, g, K)   # n+1번 직원 결정하러 이동
#         A[n] = 1    # n번 직원 참여
#         f(n+1, g, K)

T = int(input())
for tc in range(T):
    N, K = map(int, input().split())
    heights = list(map(int, input().split()))
    A = [0]*N   # 탑에 포함되었는지 표시
    minV = 100000000
    f1(0, N, K, 0)
    print(f'#{tc+1} {minV}')