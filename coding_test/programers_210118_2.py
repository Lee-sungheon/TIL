# 하노이 탑

def solution(n):
    answer = []
    def move(cnt, start, end, tmp):
        if cnt <= 1:
            answer.append([start, end])
            return
        move(cnt-1, start, tmp, end)
        answer.append([start, end])
        move(cnt-1, tmp, end, start)
    move(n, 1, 3, 2)
    return answer


print(solution(2))