def solution(places):
    delta = [[0, 1], [1, 0], [-1, 0], [0, -1]]

    def dfs(place, x, y, dep):
        nonlocal isTrue
        if dep >= 2:
            return
        for dx, dy in delta:
            nx = x + dx
            ny = y + dy
            if nx < 0 or ny < 0 or nx > 4 or ny > 4:
                continue
            if place[ny][nx] == 'P' and not visited[ny][nx]:
                isTrue = False
                return
            elif place[ny][nx] == 'X':
                continue
            elif place[ny][nx] == 'O' and not visited[ny][nx]:
                dfs(place, nx, ny, dep+1)
                visited[ny][nx] = True;

    answer = []

    for place in places:
        isTrue = True
        visited = [[False]*5 for _ in range(5)]
        for i in range(5):
            for j in range(5):
                if place[i][j] == 'P' and isTrue:
                    visited[i][j] = True;
                    dfs(place, j, i, 0)
        if isTrue:
            answer.append(1)
        else:
            answer.append(0)

    return answer


print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPXX", "OXXXP", "POOXX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))