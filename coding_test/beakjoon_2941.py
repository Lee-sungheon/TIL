# 크로아티아 알파벳

words = input()

words = words.replace('dz=','a')
words = words.replace('c=', 'a')
words = words.replace('c-', 'a')
words = words.replace('d-', 'a')
words = words.replace('lj', 'a')
words = words.replace('nj', 'a')
words = words.replace('s=', 'a')
words = words.replace('z=', 'a')

print(len(words))