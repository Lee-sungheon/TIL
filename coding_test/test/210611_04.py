def fountainActivation(locations):
    dp = [-1] * locations_count
    for i in range(locations_count):
        left = max(i - locations[i], 0)
        right = min(i + (locations[i] + 1), locations_count)
        dp[left] = max(dp[left], right)
    print(dp)
    cnt = 1
    idx_right = dp[0]
    idx_next = 0
    for i in range(locations_count):
        idx_next = max(idx_next, dp[i])
        if i == idx_right:
            cnt += 1
            idx_right = idx_next
    return cnt

if __name__ == '__main__':
    locations_count = int(input().strip())

    locations = []

    for _ in range(locations_count):
        locations_item = int(input().strip())
        locations.append(locations_item)

    result = fountainActivation(locations)
    print(result)

    # print(fountainActivation([1, 1, 1]))
    # print(fountainActivation([2, 0, 0, 0]))