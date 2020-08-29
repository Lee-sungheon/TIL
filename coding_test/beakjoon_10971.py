# 외판원 순회2

def dfs(start, next, value, visited):
    if len(visited) == N:
        if cities[next][start] != 0:
            min_value[0] = min(min_value[0], value + cities[next][start])
        return
    for w in range(N):
        if cities[next][w] != 0 and w not in visited:
            visited.append(w)
            if value + cities[next][w] < min_value[0]:
                dfs(start, w, value + cities[next][w], visited)
            visited.pop()


N = int(input())
cities = [list(map(int, input().split())) for _ in range(N)]
min_value = [100000000]
for i in range(N):
    dfs(i, i, 0, [i])
print(min_value[0])