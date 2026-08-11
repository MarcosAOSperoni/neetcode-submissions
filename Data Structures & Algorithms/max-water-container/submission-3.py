class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # we will have 2 pointers
        l,r = 0, len(heights) -1
        mostW = 0
        while l < r:
            #print(f"l={l} r={r}, max= {mostW} curr{(min(heights[l], heights[r]) * (r - l))}")
            mostW = max(mostW, (min(heights[l], heights[r]) * (r - l)) )
            if heights[l] < heights[r]:
                l +=1
            else:
                r -=1
        return mostW

                
            
