def kidsWithCandies(candies, extraCandies):
    result = []
    for i in range(len(candies)):
        if candies[i]+extraCandies >= max(candies):
            result.append(True)
        else:
            result.append(False)
    return result


def main():
    candies = [2, 3, 5, 1, 3]
    extraCandies = 3
    result = kidsWithCandies(candies, extraCandies)
    print(result)


main()
