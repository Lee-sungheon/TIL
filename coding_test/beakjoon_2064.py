# IP 주소
N = int(input())
ip_lists = [list(map(int, input().split('.'))) for _ in range(N)]
cnt_lists = [0]*4
address = ['0b']*4
mask = ['0b']*4

for i in range(N):
    for j in range(4):
        ip_lists[i][j] = '0b' + format(ip_lists[i][j], 'b').zfill(8)
ip_lists.sort()
for i in range(4):
    for j in range(2, 10):
        cnt = []
        for k in range(N):
            cnt.append(ip_lists[k][i][j])
        if cnt.count(cnt[0]) == N:
            cnt_lists[i] += 1
        else:
            break
for i in range(1, 4):
    if cnt_lists[i-1] != 8:
        cnt_lists[i] = 0

for i in range(4):
    for j in range(cnt_lists[i]):
        address[i] += ip_lists[0][i][j+2]
    for j in range(cnt_lists[i], 8):
        address[i] += '0'

for i in range(4):
    for _ in range(cnt_lists[i]):
        mask[i] += '1'
    for _ in range(8-cnt_lists[i]):
        mask[i] += '0'

for i in range(N):
    print(ip_lists[i])
print(cnt_lists)
print(address)
print(mask)

print(f'{int(address[0], 2)}.{int(address[1], 2)}.{int(address[2], 2)}.{int(address[3], 2)}')
print(f'{int(mask[0], 2)}.{int(mask[1], 2)}.{int(mask[2], 2)}.{int(mask[3], 2)}')