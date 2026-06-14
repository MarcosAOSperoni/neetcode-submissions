class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        found = True
        out = right
        while left <= right:
            k = (left + right) // 2
            time = 0
            for p in piles:
                time += math.ceil(p / k)

            if time <= h:
                out = min(out, k)
                right = k - 1
            else:
                left = k + 1
        return out