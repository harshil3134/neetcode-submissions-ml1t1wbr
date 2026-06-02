class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None
        
        interval = 1
        # Keep pairing up lists until only 1 master list is left at index 0
        while interval < len(lists):
            for i in range(0, len(lists) - interval, interval * 2):
                lists[i] = self.mergetwo(lists[i], lists[i + interval])
            interval *= 2
            
        return lists[0]
    
    def mergetwo(self, l1, l2):
        res = dummy = ListNode(0)

        while l1 and l2:
            if l1.val < l2.val:
                res.next = l1  
                l1 = l1.next
            else:
                res.next = l2 
                l2 = l2.next
            res = res.next
        
        
        if l1:
            res.next = l1
        if l2:
            res.next = l2
        
        return dummy.next