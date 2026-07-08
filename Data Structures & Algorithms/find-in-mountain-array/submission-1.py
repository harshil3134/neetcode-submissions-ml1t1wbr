class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        
        # An order-agnostic binary search helper
        def binarysearch(low, high, is_ascending):
            while low <= high:
                mid = (low + high) // 2
                val = mountainArr.get(mid)
                
                if val == target:
                    return mid
                
                if is_ascending:
                    if val > target:
                        high = mid - 1
                    else:
                        low = mid + 1
                else:  # Descending order logic
                    if val > target:
                        low = mid + 1  # Smaller values are to the right
                    else:
                        high = mid - 1 # Larger values are to the left
            return -1

        # 1. Find the Peak Index
        low, high = 0, mountainArr.length() - 1
        while low < high:
            mid = (low + high) // 2
            if mountainArr.get(mid) < mountainArr.get(mid + 1):
                low = mid + 1
            else:
                high = mid
        peak_index = low
        
        # 2. Search the left (ascending) side
        search1 = binarysearch(0, peak_index, is_ascending=True)
        if search1 != -1:
            return search1 # The problem asks for the minimum index, so return left immediately if found
            
        # 3. Search the right (descending) side
        return binarysearch(peak_index + 1, mountainArr.length() - 1, is_ascending=False)