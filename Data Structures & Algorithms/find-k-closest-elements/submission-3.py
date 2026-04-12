class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        res = []
        ind = self.binarysearch(arr, x, 0, len(arr) - 1)
        
        l = ind - 1
        r = ind
        
        while len(res) < k:
            # Check if left is valid and right is valid
            if l >= 0 and r < len(arr):
                dist_l = abs(arr[l] - x)
                dist_r = abs(arr[r] - x)
                
                # Tie-breaker: if distances are equal, pick the smaller (left) one
                if dist_l <= dist_r:
                    res.append(arr[l])
                    l -= 1
                else:
                    res.append(arr[r])
                    r += 1
            
            # If we've run out of elements on the right
            elif l >= 0:
                res.append(arr[l])
                l -= 1
            
            # If we've run out of elements on the left
            elif r < len(arr):
                res.append(arr[r])
                r += 1
        
        # Sort once at the end and return
        return sorted(res)

    def binarysearch(self, arr, target, start, end) -> int:
        if start > end:
            return start
        mid = (start + end) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            return self.binarysearch(arr, target, mid + 1, end)
        else:
            return self.binarysearch(arr, target, start, mid - 1)