def solution(enter, leave):
    answer = []
    room = []
    N = len(enter)
    cnt = [[0]*(N+1) for _ in range((N+1))]
    while True:
        if enter:
            room.append(enter.pop(0))
        if room[-1] == leave[0]:
            n = len(room)
            if n > 1:
                for i in range(n):
                    for j in range(n):
                        if room[i] != room[j]:
                            cnt[room[i]][room[j]] += 1
            room.pop(-1)
            leave.pop(0)
            while True:
                if leave and leave[0] in room:
                    room.pop(room.index(leave[0]))
                    leave.pop(0)
                else:
                    break
        if len(leave) == 0:
            break
    for i in range(1, N+1):
        answer.append(N-cnt[i].count(0)+1)
    return answer

solution([1,3,2], [1,2,3])
solution([1,4,2,3], [2,1,3,4])
solution([3,2,1], [2,1,3])
solution([3,2,1], [1,3,2])
solution([1,4,2,3], [2,1,4,3])