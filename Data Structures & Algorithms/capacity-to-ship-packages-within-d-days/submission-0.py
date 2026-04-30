class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        # The minimum capacity must be at least the heaviest item (max(weights))
        # The maximum capacity would be the sum of all weights (sum(weights))
        start = max(weights)
        end = sum(weights)
        prev = 0

        # Binary Search on the possible capacity "mid"
        while start <= end:
            mid = (start + end) // 2
            
            wsum = 0     # Current weight on the current ship
            dcal = 1     # Current day count
            s = 0        # Pointer for the weights array
            
            # Simulate shipping process with capacity "mid"
            while s < len(weights):
                # If adding the next item stays within capacity, add it
                if (wsum + weights[s]) <= mid:
                    wsum += weights[s]
                    s += 1
                # Otherwise, move to the next day and reset the current ship's weight
                else:
                    dcal += 1
                    wsum = 0
                
                # Optimization: if we exceed allowed days, stop this simulation early
                if dcal > days:
                    break
            
            # If dcal > days, the capacity 'mid' is too small; we need more capacity
            if dcal > days:
                start = mid + 1
            # If dcal <= days, 'mid' works! Store it and try to find a smaller capacity
            else:
                prev = mid
                end = mid - 1
            
        return prev