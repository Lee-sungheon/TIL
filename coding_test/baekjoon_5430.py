from collections import deque
import sys

input = sys.stdin.readline

for tc in range(int(input())):
    p = input().rstrip()
    n = int(input())
    array = input().rstrip()
    if n == 0:
        array = deque()
    else:
        array = deque(map(str, array[1:len(array)-1].split(',')))
    if "RR" in p:
        p = p.replace("RR", "")
    i = 0
    is_reverse = False
    while i < len(p):
        if p[i] == 'D':
            if array:
                if is_reverse:
                    array.pop()
                else:
                    array.popleft()
            else:
                print("error")
                break
        elif p[i] == "R":
            is_reverse = not is_reverse
        i += 1
    else:
        if is_reverse:
            array.reverse()
        print('['+ ','.join(list(array)) + ']')