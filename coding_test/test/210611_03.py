
# a + b = 29
# a ^ b = 25
# a ^ (29 - a) = 25
# a ^ 29 - a ^ a = 25

def bitwiseEquations(a, b):
    result = []
    for i in range(len(a)):
        if a[i] < b[i]:
            result.append(0)
        else:
            dif = a[i] - b[i]
            tmp = []
            tot = 0
            for j in range(51, -1, -1):
                if b[i] & (1 << j):
                    tmp.append(b[i] & (1 << j))
                elif dif >= (1 << j) * 2:
                    dif -= (1 << j) * 2
                    tot += 1 << j
            if dif == 0:
                result.append((a[i]-sum(tmp)-tot)*2 + (sum(tmp)+tot)*3)
            else:
                result.append(0)
    return result

if __name__ == '__main__':
    a_count = int(input().strip())
    a = []
    for _ in range(a_count):
        a_item = int(input().strip())
        a.append(a_item)
    b_count = int(input().strip())
    b = []
    for _ in range(b_count):
        b_item = int(input().strip())
        b.append(b_item)
    result = bitwiseEquations(a, b)
    print(result)
