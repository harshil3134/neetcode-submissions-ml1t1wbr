class ListNode:
    def __init__(self,val, nxt=None,prev=None):
        self.val=val
        self.next=nxt
        self.prev=prev

class MyCircularQueue:

    def __init__(self, k: int):
        self.head=None
        self.tail=None
        self.size=0
        self.capacity=k

    def enQueue(self, value: int) -> bool:
        if self.isFull(): 
            return False
        
        if self.head is None:
            new_node = ListNode(value)
            new_node.next = new_node
            new_node.prev = new_node
            self.head = new_node
            self.tail = new_node
        

        else:
            new_node = ListNode(value, nxt=self.head, prev=self.tail)
            self.tail.next = new_node
            self.head.prev = new_node
            self.tail = new_node  # Move tail pointer to the new end
            
        self.size += 1
        return True
            

    def deQueue(self) -> bool:

        if self.isEmpty(): 
            return False

        if self.head==self.tail:
            self.head=None
            self.tail=None
        else:
            self.tail.next=self.head.next
            self.head.next.prev=self.tail
            self.head=self.head.next
        self.size-=1
        return True

        

    def Front(self) -> int:
        if self.isEmpty():
            print("isem")
            return -1
        
        return self.head.val

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        
        return self.tail.val
        

    def isEmpty(self) -> bool:
        if self.head==None:
            return True
        else:
            return False

    def isFull(self) -> bool:
        if self.size==self.capacity:
            return True
        else:
            return False


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()