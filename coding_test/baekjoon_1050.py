# 물약 (문자열)
N, M = map(int, input().split())
result = 1000000001
items = {}
combinations = {}
for _ in range(N):
    a, b = input().split()
    items[a] = int(b)
for _ in range(M):
    tmp = input().split('=')
    tmp[1] = tmp[1].split('+')
    if tmp[0] in combinations:
        combinations[tmp[0]].append(tmp[1][:])
    else:
        combinations[tmp[0]] = [tmp[1][:]]
for _ in range(M):
    for key in combinations:
        for i in range(len(combinations[key])):
            value = 0
            for j in range(len(combinations[key][i])):
                if combinations[key][i][j][1:] not in items:
                    value = 0
                    break
                value += int(combinations[key][i][j][:1]) * items[combinations[key][i][j][1:]]
            if value:
                if key not in items:
                    items[key] = value
                else:
                    items[key] = min(value, items[key])
if "LOVE" in items:
    result = min(result, items["LOVE"])
else:
    result = -1
print(result)
