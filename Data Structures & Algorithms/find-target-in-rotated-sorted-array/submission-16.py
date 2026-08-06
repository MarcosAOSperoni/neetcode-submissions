class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l+r) // 2
            if nums[m] == target:
                return m
            # check if arr is sorted
            if nums[l] <= nums[r]:
                # check if in left
                if nums[l] <= target <= nums[m]:
                    # go left
                    r = m - 1
                # else go right
                else:
                    l = m + 1

            # check if left is sorted
            elif nums[l] <= nums[m]:
                # is target in left?
                if nums[l] <= target <= nums[m]:
                    # go left
                    r = m - 1
                # else go right
                else: l = m + 1

            # right must be sorted 
            else:
                # is target in right?
                if nums[m] <= target <= nums[r]:
                    # go right
                    l = m + 1
                # else go left
                else:
                    r = m -1
        return -1
