from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        point1 = len(matrix)-1
        point2 = 0

        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False

        while point1 >= 0 and point2 < len(matrix[0]):
            if matrix[point1][point2] < target:
                point2 += 1
            elif matrix[point1][point2] > target:
                point1 -= 1
            else:
                return True

        return False


if __name__ == "__main__":
    s = Solution()
    print(s.searchMatrix([[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [
          3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]], 5))
