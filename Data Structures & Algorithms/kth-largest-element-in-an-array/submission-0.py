class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        data=nums
        largest=0
        while k!=0:
            heapq._heapify_max(data)
            largest=heapq.heappop_max(data)
            k-=1


        return largest