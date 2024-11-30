from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        num_dict = {}

        for num in nums:
            if num in num_dict:
                num_dict.pop(num)
            else:
                num_dict[num] = 1

        return list(num_dict.keys())[0]
