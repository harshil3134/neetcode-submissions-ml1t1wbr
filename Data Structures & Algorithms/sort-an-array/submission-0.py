import random

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.quicksort(nums, 0, len(nums) - 1)
        return nums

    def quicksort(self,  nums: List[int],start:int,end:int):
          if start<end:
            p_id=self.partition(nums,start,end)

            self.quicksort(nums,start,p_id-1)
            self.quicksort(nums,p_id+1,end)

    def partition(self,nums:List[int],start:int,end:int)->int:
            rand_idx=random.randint(start,end)
            nums[rand_idx],nums[end]=nums[end],nums[rand_idx]

            pivot=nums[end]
            i=start-1

            for j in range(start,end):
                if nums[j]<=pivot:
                    i+=1
                    nums[i],nums[j]=nums[j],nums[i]
            
            nums[i+1],nums[end]=nums[end],nums[i+1]

            return i+1
