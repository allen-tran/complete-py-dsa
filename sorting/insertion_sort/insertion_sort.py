from typing import List


class Solution:
    def insertion_sort(self, arr: List[int]) -> List[int]:
        for i in range(1, len(arr)):
            j = i

            while arr[j-1] > arr[j] and j > 0:
                arr[j-1], arr[j] = arr[j], arr[j-1]
                j -= 1
        return arr


if __name__ == "__main__":
    s = Solution()
    print(s.insertion_sort([3, 5, 6, 2, 5, 7, 8, 9, 6, 4, 2]))
