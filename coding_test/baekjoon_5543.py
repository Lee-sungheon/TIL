# 햄버거 세트 가격

total = -50
min_price1 = min_price2 = 3000
for i in range(5):
    price = int(input())
    if i <= 2:
        if(price < min_price1):
            min_price1 = price
    else :
        if(price < min_price2):
            min_price2 = price

total += min_price1
total += min_price2

print(total)