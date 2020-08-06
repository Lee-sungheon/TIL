# 다이얼

words = input()
time = 0

for word in words:
    if word in 'ABC':
        time += 3
    elif word in 'DEF':
        time += 4
    elif word in 'GHI':
        time += 5
    elif word in 'JKL':
        time += 6
    elif word in 'MNO':
        time += 7
    elif word in 'PQRS':
        time += 8
    elif word in 'TUV':
        time += 9
    elif word in 'WXYZ':
        time += 10
    
print(time)