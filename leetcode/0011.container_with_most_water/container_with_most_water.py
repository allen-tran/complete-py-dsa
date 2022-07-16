class Solution:
    def maxArea(self, height):
        l, r = 0, len(height) - 1
        global_max = -float('inf')

        while l != r:
            area = min(height[l], height[r]) * (r-l)
            global_max = max(area, global_max)
            if height[r] > height[l]:
                l += 1
            else:
                r -= 1

        return global_max


if __name__ == "__main__":
    s = Solution()
    print(s.maxArea([]))
