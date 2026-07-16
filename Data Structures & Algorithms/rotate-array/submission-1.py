class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n  # Handle cases where k > len(nums)
        
        # Helper function to reverse a portion of the array
        def reverse(l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
        
        # 1. Reverse the entire array
        reverse(0, n - 1)
        # 2. Reverse the first k elements
        reverse(0, k - 1)
        # 3. Reverse the rest
        reverse(k, n - 1)