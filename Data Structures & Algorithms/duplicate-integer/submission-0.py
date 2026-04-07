class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        copy={}
        for i in nums:
            copy[i]=1
       
        return (len(copy)!=len(nums))