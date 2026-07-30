class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) -1

        while left <= right:
            i = (left + right) // 2
            if nums[i] < target:
                left = i + 1
            elif nums[i] > target:
                right = i -1
            elif nums[i] == target:
                return i

        return -1