class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l=0
        r=len(nums)-1

        while l<r:
            while nums[l]!=val and l<len(nums)-1:
                l+=1
            while nums[r]==val and r>0:
                r-=1
            if l<r:
                nums[l]=nums[r]
                nums[r]=val

        k=[i for i in nums if i!=val]
        return len(k)