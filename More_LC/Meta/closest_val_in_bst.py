'''
LC 270: Closest Binary Search Tree Value
Given the root of a binary search tree and a target value, return the value in the BST that is closest to the target. 
If there are multiple answers, print the smallest.
'''
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def _create_tree(arr):
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
            if arr[i] is not None and i < n:
                node.right = TreeNode(arr[i])
                q.append(node.right)
            i += 1
        return root


class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        closest_val = root.val
        while root:
            # Here the key works as follows:
            # First compare the min based on the diff
            # If both are equal then use sorting order
            closest_val = min(root.val, closest_val, key = lambda x: (abs(target - x), x))   
            if target < root.val:
                root = root.left
            else:
                root = root.right
        return closest_val

# Time Complexity: O(H) where H is the height of the tree
# Space Complexity: O(1) since we are not using any extra space

print(Solution().closestValue(_create_tree([4,2,5,1,3]), 3.714286)) 
print(Solution().closestValue(_create_tree([41,37,44,24,39,42,48,1,35,38,40,None,43,46,49,0,2,30,36,None,None,None,None,None,None,45,47,None,None,None,None,None,4,29,32,None,None,None,None,None,None,3,9,26,None,31,34,None,None,7,11,25,27,None,None,33,None,6,8,10,16,None,None,None,28,None,None,5,None,None,None,None,None,15,19,None,None,None,None,12,None,18,20,None,13,17,None,None,22,None,14,None,None,21,23]), 3.285714)) 


            
            
        