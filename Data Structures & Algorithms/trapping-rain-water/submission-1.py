class Solution:
    def trap(self, height: List[int]) -> int:
        # result
        res=0
        # 2 pointer while loop
        l,r= 0, len(height) -1
        # max Left and Right
        maxL,maxR= height[l],height[r]
        while l < r:
            if height[l] < height[r]:
                l += 1
                maxL = max(maxL, height[l])
                res += max(0, min(maxL,maxR) - height[l])
            else:
                r -= 1
                maxR = max(maxR, height[r])
                res += max(0, min(maxL,maxR) - height[r])
        return res