# 팩토리얼 꼬리 0 길이

def solution(n):
    answer = 0
    five = 1
    while n > five:
        five *= 5
        answer += n // five
    return answer


print(solution(5))
print(solution(10))