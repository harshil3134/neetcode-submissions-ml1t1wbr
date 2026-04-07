def check(nums, ele, ind):
    if ind+1>len(nums)-1:
        return -1
    for i in range(ind+1,len(nums)):
        print('num',nums[i],"==",ele)
        if nums[i]==ele:
            return i
    return -1


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for ind,ele in enumerate(nums):
            print('ele ',ele)
            res=check(nums,target-ele,ind)
            if (res!=-1) and (res>=0):
                return ([ind,res])