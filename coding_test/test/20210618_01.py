def maxDifference(px):
    max_value = -1
    min_value = px[0];
    for i in range(1, px_count):
        if px[i] > min_value:
            max_value = max(max_value, px[i] - min_value)
        min_value = min(min_value, px[i])
    return max_value

px_count = 6
maxDifference([7, 9, 5, 6, 3, 2])
px_count = 5
maxDifference([10, 8, 7, 6, 5])