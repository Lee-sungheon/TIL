# 회문

T = int(input())
for tc in range(T):
    words = list(input())
    result = 0
    length = len(words)
    
    if words[:] == list(reversed(words[:])):
            pass
    else:
        for i in range(length // 2):
            if words[i] != words[length-1-i] and (words[i] == words[length-2-i] or words[i+1] == words[length-1-i]):
                if words[i+1:length-i] == list(reversed(words[i+1:length-i])) or words[i:length-1-i] == list(reversed(words[i:length-1-i])):
                    result = 1
                    break
                else:
                    result = 2
                    break
            elif words[i] != words[length-1-i]:
                result = 2
                break

    print(result)