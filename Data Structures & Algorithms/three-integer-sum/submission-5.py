class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        res=set()
        nums.sort()
        for i in range(len(nums)-2):

            l=i+1
            r=len(nums)-1
            while(l<r):
                if nums[l]>0 and nums[r]>0 and nums[i]>0:
                    break
                elif nums[l]<0 and nums[r]<0 and nums[i]<0:
                    break
                sum=nums[i]+nums[l]+nums[r]

                if sum==0:
                    res.add(tuple(sorted([nums[i],nums[r],nums[l]])))
                    
                    l+=1
                elif sum<0:
                    l+=1
                else:
                    r-=1
        
        return list(res)
