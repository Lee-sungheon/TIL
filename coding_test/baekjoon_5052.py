# 전화번호 목록
import sys
def input():
    return sys.stdin.readline()[:-1]


T = int(input())
for tc in range(T):
    n = int(input())
    nums = [input() for _ in range(n)]
    nums.sort()
    result = "YES"
    for i in range(1, n):
        a = len(nums[i-1])
        b = len(nums[i])
        if a >= b:
            sli = b
        else:
            sli = a
        if nums[i-1][:sli] == nums[i][:sli]:
            result = "NO"
            break
    print(result)
