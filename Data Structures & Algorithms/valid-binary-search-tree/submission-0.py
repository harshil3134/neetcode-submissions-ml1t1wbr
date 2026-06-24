class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node, low, high):
            # Base Case: An empty tree/node is always a valid BST
            if not node:
                return True
            
            # The current node's value MUST stay strictly within its boundaries
            if not (low < node.val < high):
                return False
            
            # Go left: update the high boundary to node.val
            # Go right: update the low boundary to node.val
            return dfs(node.left, low, node.val) and dfs(node.right, node.val, high)

        # Start the recursion with negative and positive infinity as boundaries
        return dfs(root, float('-inf'), float('inf'))