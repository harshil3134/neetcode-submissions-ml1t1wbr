class Solution:
    def trap(self, height: List[int]) -> int:
        maxl=[]
        maxr=[]
        max=height[0]
        for i,v in enumerate(height):
            maxl.append(max)
            if v>max:
                max=v
        max=height[-1]
        for v in reversed(height):
            maxr.append(max)
            if v>max:
                max=v
        maxr.reverse()
        water=0
        colsum=0
        ans=0
        for i,v in enumerate(height):
            ans=min(maxl[i],maxr[i])-height[i]
            if ans>0:
                colsum=colsum+ans
        
        
        return colsum
            