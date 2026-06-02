# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        rlist=ListNode(0)
        i=1
        if len(lists)==0:
            return None
        if len(lists)==1:
            return lists[0]
        while i<len(lists):
            # print("i-1 list")
            # self.iterateli(lists[i-1])
            # print("i list")
            # self.iterateli(lists[i])
            lists[i]=self.mergetwo(lists[i-1],lists[i])
            # print("i after list")
            # self.iterateli(lists[i])
            i+=1
        # rlist=self.mergetwo(lists[0],lists[1])
        
        return lists[i-1]
    
    def iterateli(self,l1):
        while l1:
            print(l1.val)
            l1=l1.next

    
    def mergetwo(self,l1,l2):
        res=dummy= ListNode(0)

        while l1 and l2:

            if l1.val<l2.val:
                res.next=ListNode(l1.val)
                l1=l1.next
            else:
                res.next=ListNode(l2.val)
                l2=l2.next
            res=res.next
        
        while l1:
            res.next=ListNode(l1.val)
            l1=l1.next
            res=res.next
        
        while l2:
            res.next=ListNode(l2.val)
            l2=l2.next
            res=res.next
        
        return dummy.next


