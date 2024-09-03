def largestAltitude(gain):
    alt = 0
    highest = 0
    for dif in gain:
        alt += dif
        if alt > highest:
            highest = alt

    return highest


def main():
    gain = [-4, -3, -2, -1, 4, 3, 2]
    print(largestAltitude(gain))


main()
