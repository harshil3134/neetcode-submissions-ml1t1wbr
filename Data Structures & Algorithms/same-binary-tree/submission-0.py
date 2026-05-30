# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        self.height=0
        parr=[]
        qarr=[]
        self.traverse(p,parr)
        self.traverse(q,qarr)
        return parr==qarr


    def traverse(self, root,arr):

        if root==None:
            arr.append(None)
            return
        
        if root.left==root.right==None:
            arr.append(root.val)
            return 

        if root.left:
            self.traverse(root.left,arr)
        else:
            arr.append(None)
        arr.append(root.val)

        if root.right:
            self.traverse(root.right,arr)
        else:
            arr.append(None)
            