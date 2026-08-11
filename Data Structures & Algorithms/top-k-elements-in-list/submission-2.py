class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # we should use bucket sort

        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        # loop through and count
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        # go through count and place them in freq
        for n, c in count.items():
            freq[c].append(n)
        # go through freq reverse and add them to res
        res = []
        for i in range(len(freq) - 1, 0 , -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res

        
