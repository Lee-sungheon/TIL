# 단어 정렬

n = int(input())
array = [input() for _ in range(n)]
array = list(set(array))
array.sort(key = lambda x : (len(x), x))
for arr in array:
    print(arr)