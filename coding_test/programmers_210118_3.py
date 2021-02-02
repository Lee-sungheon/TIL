# 최대공약수와 최소공배수

def solution(n, m):
    answer = []
    def gcd(a, b):
        while b != 0:
            r = a%b
            a = b
            b = r
        return a
    answer.append(gcd(n, m))
    answer.append((n*m)//answer[0])
    return answer