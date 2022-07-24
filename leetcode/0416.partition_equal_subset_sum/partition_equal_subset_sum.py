import time
from typing import List


class BruteForceSolution:
    def canPartition(self, nums: List[int]) -> bool:
        """brute force with no memoization

        Returns:
            bool:  determines if can partition with subsets equal to sum
        """
        s = sum(nums)
        if s % 2 != 0:
            return False
        s /= 2

        return self.recursive(nums, s, 0)

    def recursive(self, nums, s, index):
        if s == 0:
            return True

        if index >= len(nums) or len(nums) == 0:
            return False

        if nums[index] <= s:
            if self.recursive(nums, s-nums[index], index+1):
                return True

        return self.recursive(nums, s, index+1)


class DpMemoSolution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)

        if s % 2 != 0:
            return False

        s /= 2

        dp = [[-1 for x in range(int(s)+1)] for y in range(len(nums))]

        return True if self.recursive(dp, nums, int(s), 0) == 1 else False

    def recursive(self, dp, nums, s, index):
        if s == 0:
            return 1

        if index >= len(nums) or len(nums) == 0:
            return 0

        if dp[index][s] == -1:
            if nums[index] <= s:
                if self.recursive(dp, nums, s - nums[index], index+1) == 1:
                    dp[index][s] = 1
                    return 1

        dp[index][s] = self.recursive(dp, nums, s, index+1)

        return dp[index][s]


class DpTabulationSolution:
    def canPartition(self, nums: List[int]) -> bool:
        """dp with tabulation

        Returns:
            bool:  determines if can partition with subsets equal to sum
        """

        s = sum(nums)
        if s % 2 != 0:
            return False
        s /= 2

        return self.recursive(nums, s, 0)


if __name__ == "__main__":
    bf = BruteForceSolution()
    m = DpMemoSolution()
    t = DpTabulationSolution()

    start = time.time()
    print(bf.canPartition([1, 5, 11, 5]))
    end = time.time()
    print(f"Brute Force Time: {end - start}")

    new_start = time.time()
    print(m.canPartition([1, 5, 11, 5]))
    new_end = time.time()
    print(f"Memoization Time: {new_end - new_start}")

    # print(t.canPartition([1, 5, 11, 5]))
