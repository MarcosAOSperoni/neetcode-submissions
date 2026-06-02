class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i in range(len(nums)):
            if map.get(target-nums[i], -1) != -1:
                return [map.get(target-nums[i]), i]
            map[nums[i]] = i