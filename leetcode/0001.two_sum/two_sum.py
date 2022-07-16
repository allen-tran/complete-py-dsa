class Solution:
    def twoSum(self, nums, target):
        numbers = {}

        for i in range(len(nums)):
            diff = target-nums[i]
            if diff in numbers:
                return [i, numbers[diff]]
            numbers[nums[i]] = i
        return


if __name__ == "__main__":
    s = Solution()

    print(s.twoSum([2, 7, 11, 15], 9))
