import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        temp = re.sub(r'[^a-z0-9]', '', s.lower())
        l, r = 0, len(temp) - 1

        while l < r:
            if temp[l] != temp[r]:
                return False
            l += 1
            r -= 1

        return True
