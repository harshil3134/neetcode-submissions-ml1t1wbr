# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head
        
        # 1. Use a dummy node so preleft always exists, even if left = 1
        dummy = ListNode(0)
        dummy.next = head
        
        curr = dummy
        pos = 0
        
        # --- YOUR FIRST LOOP (Fixed using position counter) ---
        while curr.next:
            if pos + 1 == left:
                preleft = curr
                leftpointer = curr.next
                break
            curr = curr.next
            pos += 1
            
        # Move curr onto the actual starting node for the reversal
        curr = leftpointer
        pos += 1
        
        # --- YOUR SECOND LOOP (Fixed to reverse up to the 'right' position) ---
        prev = None
        while curr and pos <= right:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
            pos += 1 # Keep tracking the position as we flip
            
        # --- YOUR RECONNECTION LOGIC (Exactly your original idea!) ---
        postright = curr
        leftpointer.next = postright
        preleft.next = prev
        
        return dummy.next