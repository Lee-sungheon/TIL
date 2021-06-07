# 최대공약수와 최대공배수
import math

def lcm(a, b):
    return a * b // math.gcd(a, b)

a, b = map(int, input().split())
print(math.gcd(a, b))
print(lcm(a, b))