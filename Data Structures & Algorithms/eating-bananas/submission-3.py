import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Start at 1 to avoid division by zero
        return self.calc(piles, 1, max(piles), h)

    def calc(self, piles, start, end, h):
        # Base case: When pointers meet, we found the minimum speed
        if start == end:
            return start
        
        mid = (start + end) // 2
        total_hours = 0
        
        for i in piles:
            total_hours += math.ceil(i / mid)

        if total_hours <= h:
            # If it works, this 'mid' might be the answer, 
            # so we keep it in our range [start, mid]
            return self.calc(piles, start, mid, h)
        else:
            # If it doesn't work, mid is too slow, try [mid + 1, end]
            return self.calc(piles, mid + 1, end, h)