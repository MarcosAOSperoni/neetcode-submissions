class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        match = {}
        for i in range(len(nums)):
            if match.get(target - nums[i], -1) != -1:
                return [match.get(target-nums[i]), i]
            match[nums[i]] = i
