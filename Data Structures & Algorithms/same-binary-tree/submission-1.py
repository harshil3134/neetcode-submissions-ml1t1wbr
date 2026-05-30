class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Base Case 1: Both nodes are None -> structurally identical so far
        if not p and not q:
            return True
        
        # Base Case 2: One node is None but the other isn't -> structures don't match
        if not p or not q:
            return False
        
        # Base Case 3: The values don't match
        if p.val != q.val:
            return False
        
        # Recursive Step: Check if both left subtrees and right subtrees match
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)