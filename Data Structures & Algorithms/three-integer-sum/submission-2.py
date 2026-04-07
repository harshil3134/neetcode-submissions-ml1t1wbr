class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []

        nums.sort()

        for i, v in enumerate(nums):

            if v > 0:
                break

    
            if i > 0 and v == nums[i - 1]:
                continue
            
         
            l, r = i + 1, len(nums) - 1
            
            while l < r:
                current_sum = v + nums[l] + nums[r]

                if current_sum == 0:
                 
                    res.append([v, nums[l], nums[r]])
                    
                   
                    l += 1
                    r -= 1
                    
                   
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1

                elif current_sum > 0:
                  
                    r -= 1
                else: 
    
                    l += 1

        return res