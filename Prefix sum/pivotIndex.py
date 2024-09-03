def pivotIndex(nums):
    currentSum = 0
    leftSum = [currentSum]
    rightSum = [currentSum]
    for i in range(len(nums)-1):
        currentSum += nums[i]
        leftSum.append(currentSum)
    currentSum = 0
    for j in range(len(nums)-1, 0, -1):
        currentSum += nums[j]
        rightSum.append(currentSum)
    rightSum.reverse()

    print(leftSum)
    print(rightSum)
    for k in range(len(nums)):
        if leftSum[k] == rightSum[k]:
            return k
    return -1


def main():
    nums = [2, 1, -1]
    print(pivotIndex(nums))


main()
