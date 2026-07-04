class Solution:
    def __init__(self):
        self.k = 0
        self.result = None

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.k = k
        self.traverse(root)
        return self.result

    def traverse(self, node):
        if not node or self.result is not None:
            return
        
        # 1. Search the left side first (smallest elements)
        self.traverse(node.left)
        
        # 2. Process current node
        self.k -= 1
        if self.k == 0:
            self.result = node.val
            return # Found it! Stop deeper recursion branches
            
        # 3. Search the right side
        self.traverse(node.right)