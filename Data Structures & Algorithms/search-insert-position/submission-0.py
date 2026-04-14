class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return self.binarysearch(nums,target,0,len(nums)-1)

    def binarysearch(self,arr,target,start,end):

        if start>end:
            return start
        
        mid=(start+end)//2

        if arr[mid]<target:
            return self.binarysearch(arr,target,mid+1,end)
        elif arr[mid]>target:
            return self.binarysearch(arr,target,start,mid-1)
        else:
            return mid
        