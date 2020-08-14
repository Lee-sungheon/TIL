# 호텔

def aaaa(C, hotels, i, min_costs):
    P = C // hotels[i][2]
    total = P * hotels[i][2]
    cost = P * hotels[i][1]
    C -= total
    min_costs.append(cost+ hotels[i][1])
    i = i + 1

    if i == len(hotels) - 1:
        return min_costs

    return aaaa(C, hotels, i, min_costs)

C, N = map(int, input().split())
hotels = [[0] + list(map(int, input().split())) for _ in range(N)]
for i in range(len(hotels)):
    hotels[i][0] = round(hotels[i][2] / hotels[i][1], 2)

hotels.sort(reverse=True)
min_costs = []
min_costs = aaaa(C, hotels, 0, min_costs)
print(min_costs)