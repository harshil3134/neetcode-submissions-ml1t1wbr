# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.li=[]
        self.traverse(root)
        # print("ans",root)
        return root
    def traverse(self, root):
        if root==None:
            return 
        if root.left==root.right==None:
            
            return

        if root.left:
            self.traverse(root.left)

        if root.right:
            self.traverse(root.right)
        
        root.right,root.left = root.left, root.right
        
        