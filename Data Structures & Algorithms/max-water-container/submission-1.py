class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max=0
        l=0
        r=len(heights)-1
        print(heights[r])
        mh=0
        area=0
        while l<r:
            mh=heights[l] if heights[l]<heights[r] else heights[r]
            area=(mh*(r-l))
            if area>max:
                max=area

            if heights[r]>heights[l]:
                l+=1
            else:
                r-=1
        return max