class Solution:
    def trap(self, height: List[int]) -> int:
        l=0
        r=len(height)-1
        maxleft,maxright=0,0
        water=0
        while l < r:
            if height[l] < height[r]:
                if height[l] >= maxleft:
                    maxleft=height[l]
                else:
                    water+=maxleft-height[l]
                l+=1
            else:
                if height[r]>=maxright:
                    maxright=height[r]
                else:
                    water+=maxright-height[r]
                r-=1
        return water