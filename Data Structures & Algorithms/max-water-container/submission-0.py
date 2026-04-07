class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area=0
        max=0
        minh=0
        w=0
        for i,v in enumerate(heights):
            for j in range(i+1,len(heights)):
                minh=min(v,heights[j])
                w=j-i
                area=minh*w
                if area>max:
                    max=area

        return max