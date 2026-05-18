# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.li=[]
        self.traverse(root)
        return self.li
    def traverse(self, root):
        if root==None:
            return 
        
        self.li.append(root.val)


        if root.left:
            self.traverse(root.left)
        

        if root.right:
            self.traverse(root.right)
           