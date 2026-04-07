
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict={}

        for ind,ele in enumerate(nums):
            dict[ele]=ind
    
        for ind,ele in enumerate(nums):
            diff=target-ele

            if diff in dict and dict[diff]!=ind:
                return([ind,dict[diff]])