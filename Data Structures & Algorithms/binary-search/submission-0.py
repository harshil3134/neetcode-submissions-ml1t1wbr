class Solution:
    def search(self, nums: List[int], target: int) -> int:
        ind=self.binarysearch(nums,target,0,len(nums)-1)
        return ind
    

    def binarysearch(self,arr,target,start,end)-> int:

        if start>end:
            return -1
        mid=(start+end)//2

        if arr[mid]==target:
            return mid
        elif arr[mid]<target:
            return self.binarysearch(arr,target,mid+1,end)
        elif arr[mid]>target:
            return self.binarysearch(arr,target,start,mid-1)
        

