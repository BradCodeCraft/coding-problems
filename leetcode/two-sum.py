def twoSum(self, nums: List[int], target: int) -> List[int]:
    numMap = {}
    n = len(nums)

    for i in range(n):
        numMap[nums[i]] = i

    for i in range(n):
        remain = target - nums[i]

        if remain in numMap and numMap[remain] != i:
            return [i, numMap[remain]]

    return []
