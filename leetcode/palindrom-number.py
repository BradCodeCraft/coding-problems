class Solution:
    def isPalindrome(self, x: int) -> bool:
        l, r = 0, len(str(x)) - 1
        str_arr = list(str(x))

        while l < (len(str(x)) / 2):
            if str_arr[l] != str_arr[r]:
                return False
            
            l += 1
            r -= 1

        return True
