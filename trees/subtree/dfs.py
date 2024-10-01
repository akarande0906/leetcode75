# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if subRoot is None :
            return True

        if root is None :
            return False

        if self.same(root , subRoot):
            return True
        return self.isSubtree(root.left , subRoot) or self.isSubtree(root.right , subRoot)            

    def same(self , r , s):
        if r is None and s is None :
            return True
        elif not r or not s:
            return False
        else:
            if r.val != s.val:
                return False
            return self.same(r.right , s.right) and self.same(r.left , s.left)  
        
