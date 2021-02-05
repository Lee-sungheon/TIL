# 호텔 방 배정

import sys
sys.setrecursionlimit(10**6)

def solution(k, room_number):
    def find(val):
        if val not in my_dict:
            my_dict[val] = val + 1
            return val
        empty = find(my_dict[val])
        my_dict[val] = empty + 1
        return empty

    answer = []
    my_dict = dict()
    for r in room_number:
        val = find(r)
        answer.append(val)
    return answer

print(solution(10, [1,3,4,1,3,1]))