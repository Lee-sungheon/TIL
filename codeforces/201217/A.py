# Dungeon

for _ in range(int(input())):
    a, b, c = map(int, input().split())
    if (a + b + c) % 9 != 0:
        print("NO")
    else:
        r = (a + b + c) // 9
        if a < r+1 or b < r+1 or c < r+1:
            print("NO")
        else:
            print("YES")
