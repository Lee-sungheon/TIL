# 블록 이동하기
def bfs(board):
    queue = [[[0, 0], [1, 0], 0]]
    N = len(board)
    while queue:
        tmp = queue.pop(0)
        x1, y1 = tmp[0][0], tmp[0][1]
        x2, y2 = tmp[1][0], tmp[1][1]
        count = tmp[2]
        # 종료 조건 확인
        if tmp[0] == [N-1, N-1] or tmp[1] == [N-1, N-1]:
            return count
        # 오른쪽 이동
        dx1, dx2 = x1 + 1, x2 + 1
        dy1, dy2 = y1, y2
        if dx1 >= N or dx2 >= N or dy1 >= N or dy2 >= N:
            pass
        elif board[dy1][dx1] == 0 and board[dy2][dx2] == 0:
            queue.append([[dx1, dy1], [dx2, dy2], count+1])
        # 왼쪽 이동
        dx1, dx2 = x1 - 1, x2 - 1
        dy1, dy2 = y1, y2
        if dx1 < 0 or dx2 < 0 or dy1 < 0 or dy2 < 0:
            pass
        elif board[dy1][dx1] == 0 and board[dy2][dx2] == 0:
            queue.append([[dx1, dy1], [dx2, dy2], count + 1])
        # 아래 이동
        dx1, dx2 = x1, x2
        dy1, dy2 = y1 + 1, y2 + 1
        if dx1 >= N or dx2 >= N or dy1 >= N or dy2 >= N:
            pass
        elif board[dy1][dx1] == 0 and board[dy2][dx2] == 0:
            queue.append([[dx1, dy1], [dx2, dy2], count + 1])
        # # 위 이동
        # dx1, dx2 = x1, x2
        # dy1, dy2 = y1 - 1, y2 - 1
        # if dx1 < 0 or dx2 < 0 or dy1 < 0 or dy2 < 0 or dx1 >= N or dx2 >= N or dy1 >= N or dy2 >= N:
        #     pass
        # elif board[dy1][dx1] == 0 and board[dy2][dx2] == 0:
        #     queue.append([[dx1, dy1], [dx2, dy2], count + 1])
        # 회전
        if x1 == x2:
            if y1 + 1 < N and y2 + 1 < N and board[y1+1][x1] == 0 and board[y2+1][x2] == 0:
                dx1, dx2 = x1, x2 + 1
                dy1, dy2 = y1 + 1, y2
                queue.append([[dx1, dy1], [dx2, dy2], count + 1])
        else:
            if x1 + 1 < N and x2 + 1 < N and board[y1][x1+1] == 0 and board[y2][x2+1] == 0:
                dx1, dx2 = x1 + 1, x2
                dy1, dy2 = y1, y2 + 1
                queue.append([[dx1, dy1], [dx2, dy2], count + 1])


def solution(board):
    answer = bfs(board)
    return answer


print(solution([[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]))
print(solution([[0, 0, 0, 0, 0, 0, 1], [1, 1, 1, 1, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 1, 1, 0], [0, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 1, 1], [0, 0, 1, 0, 0, 0, 0]]))
print(solution([[0, 0, 0, 0, 0, 0, 1], [1, 1, 1, 1, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 1, 0, 0], [0, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 1, 0], [0, 0, 1, 0, 0, 0, 0]]))
print(solution([[0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 1, 1, 1, 0, 0], [0, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 1, 1, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1, 0]]))