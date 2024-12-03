class Solution:
    def isHappy(self, n: int) -> bool:
        def get_next(n: int) -> int:
            sum = 0
            for cur in str(n):
                sum += int(cur) ** 2
            return sum

        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = get_next(n)
        return n == 1
