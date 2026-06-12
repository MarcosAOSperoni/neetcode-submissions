class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        i = 0
        while start <= end:
            i = (start + end) // 2
            if nums[i] == target:
                return i
            if nums[i] < target:
                start = i + 1
            if nums[i] > target:
                end = i - 1
        return -1
