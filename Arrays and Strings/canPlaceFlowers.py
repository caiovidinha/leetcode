def canPlaceFlowers(flowerbed, n):
    flowers = 0
    if len(flowerbed) == 1:
        if flowerbed[0] == 0:
            flowers += 1
        else:
            flowers += 0
        return flowers >= n

    for i in range(0, len(flowerbed)):
        if (i == 0):
            if (flowerbed[i+1] == 0 and flowerbed[i] == 0):
                flowerbed[i] = 1
                flowers += 1
            continue
        if (i == len(flowerbed)-1):
            if (flowerbed[i-1] == 0 and flowerbed[i] == 0):
                flowers += 1
            return flowers >= n

        if (flowerbed[i-1] == 0 and flowerbed[i+1] == 0 and flowerbed[i] == 0):
            flowerbed[i] = 1
            flowers += 1
    return flowers >= n


def main():
    flowerbed = [1]
    n = 0
    result = canPlaceFlowers(flowerbed, n)
    print(result)


main()
