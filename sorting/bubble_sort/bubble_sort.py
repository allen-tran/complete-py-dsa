from typing import List


class Solution:
    def bubble_sort(self, nums: List[int]):
        for i in range(len(nums)):
            for j in range(len(nums)-i-1):
                if nums[j] > nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
        return nums


if __name__ == "__main__":
    s = Solution()
    print(s.bubble_sort([3, 4, 6, 7, 4, 3, 2, 56, 7, 5, 343, 2, 32, 2]))
