def maxSubArray(nums) -> int:
    # the max subarray for array of len 1 will always be the first element
    max_global = nums[0]
    # this we be the local max we always update
    curr = 0

    for i in nums:
        # at any point the local max is less than zero, we reset it
        if curr < 0:
            curr = 0
        # add the elements to local max
        curr += i
        # compare the maxes and take the highest
        max_global = max(max_global, curr)
    return max_global
