class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack)):
            if needle == haystack[i:i+len(needle)]:
                return i
        return -1


if __name__ == "__main__":
    s = Solution()
    print(s.strStr("string", "string"))
