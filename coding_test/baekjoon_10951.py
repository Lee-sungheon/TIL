# A + B - 4 ( while문 사용 )

while True:
    try:
        a, b = map(int, input().split())
        print(a + b)
    except:
        break