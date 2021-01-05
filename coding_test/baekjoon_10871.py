#X보다 작은 수

n, num = map(int,input().split())
x = list(map(int, input().split()))
for i in range(n):
    if(x[i] < num):
        print(f"{x[i]} ", end='')