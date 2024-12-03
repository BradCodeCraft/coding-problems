class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 1 if s[0] == s[1] else 2

        max_len = 0
        start = 0
        end = 0
        while end < n:
            if s[end] not in s[start:end]:
                end += 1
                max_len = max(max_len, end - start)
            else:
                start += 1

        return max_len
