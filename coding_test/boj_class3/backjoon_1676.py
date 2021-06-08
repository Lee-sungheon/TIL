# 팩토리얼 0의 개수

def solution(n):
    answer = 0
    five = 1
    while n > five:
        five *= 5
        answer += n // five
    return answer

print(solution(int(input())))