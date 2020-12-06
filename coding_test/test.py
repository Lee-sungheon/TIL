n, m = map(int, input().split())
price = {}
formula = []

for _ in range(n):
    x, p = input().split()
    p = int(p)
    price[x] = p

for _ in range(m):
    f = input()
    x, f = f.split('=')
    gs = list(map(lambda g: (int(g[0]), g[1:]), f.split('+')))
    formula.append((x, gs))

while True:
    flag = False
    print(formula)
    print(price)
    for f in formula:
        ev = 0
        for g in f[1]:
            if not g[1] in price:
                ev = None
                break
            ev += g[0]*price[g[1]]

        if ev != None:
            v = price.get(f[0])
            if v == None:
                price[f[0]] = ev
                flag = True
            elif price[f[0]] > ev:
                price[f[0]] = ev
                flag = True

    if not flag:
        break

res = price.get('LOVE')
if res == None:
    print(-1)
else:
    print(min(res, 1000000001))