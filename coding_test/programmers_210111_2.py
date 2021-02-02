#스타 수열

def solution(a):
    n = len(a)
    if n < 2:
        return 0
    else:
        answer = [0] * (n+1)
        tmp = [-1] * (n+1)
        for i in range(n):
            if i == 0:
                if a[i] != a[i+1]:
                    tmp[a[i]] = i+1
                    answer[a[i]] += 1
                continue
            if i == n-1:
                if a[i-1] != a[i] and i-1 != tmp[a[i]]:
                    answer[a[i]] += 1
                continue
            if i-1 != tmp[a[i]] and a[i-1] != a[i]:
                tmp[a[i]] = i-1
                answer[a[i]] += 1
                continue
            if i+1 != tmp[a[i]] and a[i+1] != a[i]:
                tmp[a[i]] = i+1
                answer[a[i]] += 1
    result = max(answer)
    print(answer)
    return result*2


x = [5,2,3,3,5,3]
print(solution(x))
print(solution([0]))
print(solution([0,3,3,0,7,2,0,2,2,0]))
print(solution([1,1,1,1,1,1,1,2]))

