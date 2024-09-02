def moveZeroes(nums):
    counter = 0
    i = 0
    while (i < len(nums)):
        if nums[i] == 0:
            nums.pop(i)
            counter += 1
        else:
            i += 1
    for i in range(counter):
        nums.append(0)


nums = [0, 0, 1]
moveZeroes(nums)
print(nums)
