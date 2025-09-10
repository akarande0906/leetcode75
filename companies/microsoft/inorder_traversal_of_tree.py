from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
class Solution:

    def _create_tree(self, arr):
        if not arr:
            return None
        root = TreeNode(arr[0])
        n = len(arr)
        q = [root]
        i = 1
        while i < n:
            node = q.pop(0)
            if arr[i] is not None:
                node.left = TreeNode(arr[i])
                q.append(node.left)
            i += 1
            if  i < n and arr[i] is not None:
                node.right = TreeNode(arr[i])
                q.append(node.right)
            i += 1
        return root

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return_array = []
        def traverse(root):
            if not root:
                return
            traverse(root.left)
            return_array.append(root.val)
            traverse(root.right)
        
        traverse(root)
        return return_array
    
sol = Solution()
print(sol.inorderTraversal(sol._create_tree([1,None,2,3])))
print(sol.inorderTraversal(sol._create_tree([1,2,3,4,5,None,8,None,None,6,7,9])))

# Time Complexity: O(N)
# Space Complexity: O(N) : recursion stack
