class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums) - 1):
            j = i + 1
            while j < len(nums) and nums[i] + nums[j] != target:
                j += 1
            if j < len(nums):
                return [i, j]

            