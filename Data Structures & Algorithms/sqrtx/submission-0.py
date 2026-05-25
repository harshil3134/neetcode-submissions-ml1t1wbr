class Solution:
    def mySqrt(self, x: int) -> int:
        
        ans=self.binarysearch(1,x,x)
        # print(ans)
        return ans

    def binarysearch(self,start,end,x):

        mid=(start+end)//2

        if start>end:
            return end

        if mid*mid<x:
            return self.binarysearch(mid+1,end,x)
        elif mid*mid>x:
            return self.binarysearch(start,mid-1,x)
        else:
            return mid