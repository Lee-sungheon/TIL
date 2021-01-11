words = list(input().upper())
words_list = list(set(words))
result = '?'
words_count = []
for word in words_list:
    words_count.append(words.count(word))

if words_count.count(max(words_count)) > 1:
    print(result)
else:
    print(words_list[words_count.index(max(words_count))])