class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        hig = [0, 0] # [count, value]
        i = 0
        
        while i < len(nums):
            hcount = 1 # Reset count for every new number found
            current_num = nums[i]
            
            # Move i forward while the next number is the same
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                hcount += 1
                i += 1
            
            # Check if this group is the biggest so far
            if hcount > hig[0]:
                hig[0] = hcount
                hig[1] = current_num
            
            i += 1 # Move to the next unique number
            
        return hig[1]