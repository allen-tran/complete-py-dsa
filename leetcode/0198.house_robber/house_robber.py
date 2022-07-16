import typing


class Solution:
    def rob(self, nums: typing.List[int]):
        if len(nums) < 2:
            return max(nums)

        dp = [-1] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            profit1 = nums[i] + dp[i-2]
            profit2 = dp[i-1]

            dp[i] = max(profit1, profit2)
        return dp[-1]


if __name__ == "__main__":
    s = Solution()
    print(s.rob([2, 7, 9, 3, 1]))
