# Last Year's Substring

for _ in range(int(input())):
    n = int(input())
    s = input()
    result = "2020"
    for i in range(5):
        if s[:i]+s[i+n-4:] == result:
            print("YES")
            break
    else:
        print("NO")