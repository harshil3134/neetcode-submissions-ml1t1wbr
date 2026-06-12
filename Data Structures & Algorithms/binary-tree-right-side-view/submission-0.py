# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        self.levels_map={}
        self.traverse(root,0)
        li=[arr[-1] for arr in list(self.levels_map.values())]
        return li

    def traverse(self,root, level):

        if not root:
            return
        
        if level not in self.levels_map:
            self.levels_map[level] = []
            
        # Append the current node's value to its corresponding level list
        self.levels_map[level].append(root.val)

        if root.left:
            self.traverse(root.left,level+1)
        
        if root.right:
            self.traverse(root.right,level+1)
            
