class Solution:
    def binarysearch(self, nums, start, end, target):
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
        return -1

    def search(self, nums: List[int], target: int) -> int:
        if not nums: return -1
        
        # 1. Correct Pivot Search (Finding the index of the minimum element)
        start, end = 0, len(nums) - 1
        while start < end:
            mid = (start + end) // 2
            if nums[mid] > nums[end]:
                start = mid + 1
            else:
                end = mid
        
        # 'start' is now the pivot index (index of the smallest element)
        pivot = start
        
        # 2. Decide which half to search based on the pivot
        if target >= nums[pivot] and target <= nums[len(nums) - 1]:
            # Search the right side
            return self.binarysearch(nums, pivot, len(nums) - 1, target)
        else:
            # Search the left side
            return self.binarysearch(nums, 0, pivot - 1, target)