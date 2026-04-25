# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        first=head
        second=head
        prev=head
        for i in range(n):
            first=first.next
            if first==None:
                break

        while (first!=None):
            
            first=first.next
            prev=second
            second=second.next
            if first==None:
                break
        
        if prev==second:
            head=second.next
        else:
            prev.next=second.next



        return head
            
                
