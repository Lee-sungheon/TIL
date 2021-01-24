# 피보나치 수 6

def fibo(n):
    num = 1000000007
    if dict_fibo.get(n) != None:
        return dict_fibo[n]
    else:
        if n % 2:
            f = (fibo((n + 1) // 2) % num) ** 2 + (fibo(n // 2) % num) ** 2
        else:
            f1 = fibo(n // 2 - 1) % num
            f2 = fibo(n // 2) % num
            f = ((f1 + f2) * f2 + f2 * f1) % num
            dict_fibo[n] = f % num
        return f % num

s = int(input())
dict_fibo = {0: 0, 1: 1}
print(fibo(s))
