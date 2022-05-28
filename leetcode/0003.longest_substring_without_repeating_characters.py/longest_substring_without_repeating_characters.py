def lengthOfLongestSubstring(self, s: str) -> int:
    left = 0
    letter_set = set()
    max_len = 0

    for i in range(len(s)):
        while s[i] in letter_set:
            letter_set.remove(s[left])
            left += 1

        letter_set.add(s[i])
        max_len = max(max_len, i - left+1)

    return max_len
