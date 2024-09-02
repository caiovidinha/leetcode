def productExceptSelf(nums):
    n = len(nums)
    prefix = [1] * n
    sufix = [1] * n

    for i in range(1, n):
        prefix[i] *= prefix[i-1] * nums[i-1]

    for j in range(n-2, -1, -1):
        sufix[j] *= sufix[j+1] * nums[j+1]

    for k in range(n):
        nums[k] = prefix[k] * sufix[k]
    return nums


def main():
    nums = [-1, 1, 0, 3, -3]
    result = productExceptSelf(nums)
    print(result)


main()
