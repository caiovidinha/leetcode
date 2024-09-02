def maxArea(height):
    start = 0
    end = len(height) - 1
    area = 0
    max_area = 0

    while start <= end:
        area = (end-start) * min(height[start], height[end])
        if area > max_area:
            max_area = area
        if height[start] >= height[end]:
            end -= 1
        else:
            start += 1
    return max_area


def main():
    height = [1, 1]
    print(maxArea(height))


main()
