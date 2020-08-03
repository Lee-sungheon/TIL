# 알파벳 찾기

S = input()
result = [-1] * 26

for i in range(len(S)):
    if result[ord(S[i]) - 97] == -1:
        result[ord(S[i]) - 97] = i

for res in list(map(str, result)):
    print(f'{res} ', end='')