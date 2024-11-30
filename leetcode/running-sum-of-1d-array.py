class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        result = nums
        
        for index in range(1, len(nums)):
            result[index] = result[index - 1] + nums[index]
        
        return result
