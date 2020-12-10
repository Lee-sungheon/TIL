import sys

for tc in range(int(sys.stdin.readline().rstrip())):
    N = int(sys.stdin.readline().rstrip())
    li = [sys.stdin.readline().rstrip() for _ in range(N)]
    li.sort()
    print(li)
    check = False
    for i in range(1, len(li)):
        if li[i].startswith(li[i-1]):
            check = True
    if check:
        print('NO')
    else:
        print('YES')
