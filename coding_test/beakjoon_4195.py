# 친구 네트워크
T = int(input())
for tc in range(T):
    F = int(input())
    set_li = []
    for i in range(F):
        a, b = input().split()
        tmp = []
        cnt = 0
        result = 2
        for j in range(len(set_li)):
            if a in set_li[j] or b in set_li[j]:
                set_li[j].add(a)
                set_li[j].add(b)
                tmp.append(j)
                cnt += 1
                result = len(set_li[j])
                if len(tmp) == 2:
                    set_li[tmp[0]] = set_li[tmp[0]] | set_li[tmp[1]]
                    del set_li[tmp[1]]
                    result = len(set_li[tmp[0]])
                    break
        else:
            if not cnt:
                set_li.append({a, b})
        print(result)