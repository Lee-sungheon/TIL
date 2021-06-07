# 팰린드롬수

while True:
    word = input()
    if word == '0':
        break
    reverse_word = ''.join(reversed(word))
    if reverse_word == word:
        print('yes')
    else:
        print('no')