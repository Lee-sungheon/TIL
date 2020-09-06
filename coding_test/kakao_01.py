# 실패율
def solution(N, stages=[]):
    answer = []
    fail_rate = [0]*N
    user_num = len(stages)
    for i in range(1, N+1):
        if user_num == 0:
            fail_rate[i - 1] = (0, i)
            continue
        stages_cnt = stages.count(i)
        fail_rate[i-1] = (-stages_cnt/user_num, i)
        user_num -= stages_cnt
    fail_rate.sort()
    for i in range(N):
        answer.append(fail_rate[i][1])
    return answer


print(solution(8, [1, 2, 3, 4, 5, 6, 7]))