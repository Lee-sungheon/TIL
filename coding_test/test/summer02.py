# from collections import deque

def solution(t, r):
    dq = []
    answer = []
    for i in range(len(t)):
        dq.append([t[i], i])
    dq.sort()
    for i in range(10000):
        idx = []
        for j in range(0, len(dq)):
            if dq[j][0] <= i:
                idx.append([r[dq[j][1]], dq[j][0], dq[j][1], j])
            else:
                break
        if len(idx) > 0:
            idx.sort()
            answer.append(dq.pop(idx[0][3])[1])
    return answer

solution([0,1,3,0], [0,1,2,3])
solution([0,1,3,0], [0,1,2,0])
solution([7,6,8,1], [0,1,2,3])
# print(solution([5,4,3,3], [1,2,3,4]))
solution([0,0,0,0], [1,2,3,4])