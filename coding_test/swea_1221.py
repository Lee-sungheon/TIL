T = int(input())
for tc in range(T):
    num, N = input().split()
    num_list = input().split()
    sort_list = [word for word in num_list]
    sample_list = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    for i in range(int(N)):
        sort_list[i] = sample_list.index(sort_list[i])
    sort_list.sort()
    print(f'#{tc + 1}')
    for i in sort_list:
        print(f'{sample_list[i]} ', end='')
    print()