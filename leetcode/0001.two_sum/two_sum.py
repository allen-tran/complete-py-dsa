def twoSum(nums, target):
    numbers = {}
    
    for i in range(len(nums)):
        diff = target-nums[i]
        if diff in numbers:
            return [i, numbers[diff]]
        numbers[nums[i]] = i
    return
