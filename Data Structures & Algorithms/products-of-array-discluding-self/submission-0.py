class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lef=[0 for _ in range(len(nums))]
        rig=[0 for _ in range(len(nums))]
        lef[0]=nums[0]
        rig[len(nums)-1]=nums[len(nums)-1]
        res=[]

        for i in range(len(nums)-2,-1,-1):
            rig[i]=rig[i+1]*nums[i]

        for i in range(1,len(nums)):
            lef[i]=lef[i-1]*nums[i]
        res.append(rig[1])
        for i in range(1,len(nums)-1):
            res.append(lef[i-1]*rig[i+1])
        res.append(lef[len(nums)-2])

        return res