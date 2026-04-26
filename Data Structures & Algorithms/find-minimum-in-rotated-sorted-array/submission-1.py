class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        
        # We use left < right because we want the pointers to 
        # meet at the minimum element.
        while left < right:
            mid = (left + right) // 2
            
            # If mid is greater than the rightmost element, 
            # the pivot/min is in the right half.
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                # If mid is smaller or equal, mid could be the min,
                # so we don't skip it (right = mid).
                right = mid
                
        # When left == right, we've trapped the minimum.
        return nums[left]