class Solution:
    def reverse(self, x:int) -> int:
        if x == 0:
            return 0
        elif x < 0:
            return -self.reverse(-x)
        else:
            x = int(str(x)[::-1])
            if x > 2**31 - 1:
                return 0
            return x
