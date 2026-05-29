class DoublyListNode:
    def __init__(self, key=0, val=0):
        self.key = key
        self.value = val
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.mmap = dict()  # Maps key -> DoublyListNode
        
        # Create permanent dummy boundaries
        self.head = DoublyListNode(-1, -1)
        self.tail = DoublyListNode(-1, -1)
        
        # Link them together initially
        self.head.next = self.tail
        self.tail.prev = self.head

    # Helper function: Removes a node from its current position in the list
    def _remove(self, node: DoublyListNode):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    # Helper function: Inserts a node right after the dummy head (the "newest" position)
    def _add_to_front(self, node: DoublyListNode):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        if key in self.mmap:
            node = self.mmap[key]
            # Since it was accessed, move it to the front of the list
            self._remove(node)
            self._add_to_front(node)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.mmap:
            # Update value and move it to the front
            node = self.mmap[key]
            node.value = value
            self._remove(node)
            self._add_to_front(node)
        else:
            # Check capacity; if full, evict the oldest item
            if len(self.mmap) == self.capacity:
                # Oldest item is ALWAYS right before the dummy tail
                oldest_node = self.tail.prev
                self._remove(oldest_node)
                del self.mmap[oldest_node.key]  # Remove from map using its stored key
            
            # Create the new node and insert it at the front
            new_node = DoublyListNode(key, value)
            self.mmap[key] = new_node
            self._add_to_front(new_node)