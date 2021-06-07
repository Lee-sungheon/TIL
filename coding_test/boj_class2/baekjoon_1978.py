# 소수 찾기
def find_num(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    else:
        return True

N = int(input())
nums = list(map(int, input().split()))
result = 0
for num in nums:
    if num != 1 and find_num(num):
        result += 1
print(result)