'''
LC 437: Path Sum III: Given the root of a binary tree and an integer targetSum, 
return the number of paths where the sum of the values along the path equals targetSum.
The path does not need to start or end at the root or a leaf, but it must go downwards 
(i.e., traveling only from parent nodes to child nodes).
'''

from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        count = 0
        prefix_map = {}
        def dfs(node, curr_sum):
            nonlocal count

            if not node:
                return
            curr_sum += node.val
            if curr_sum == targetSum:
                count += 1
            # We increment count by the number of times we have seen this prefix sum
            count += prefix_map.get(curr_sum - targetSum, 0) 
            prefix_map[curr_sum] = prefix_map.get(curr_sum, 0) + 1
            dfs(node.left, curr_sum)
            dfs(node.right, curr_sum)
            # Remove the current sum from the prefix sum as we have ended this path from root 
            prefix_map[curr_sum] -= 1
        dfs(root, 0)
        return count
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
            if arr[i] is not None and i < n:
                node.right = TreeNode(arr[i])
                q.append(node.right)
            i += 1
        return root
    

sol = Solution()
print (sol.pathSum(sol._create_tree([10,5,-3,3,2,None,11,3,-2,None,1]),8))
print (sol.pathSum(sol._create_tree([5,4,8,11,None,13,4,7,2,None,None,5,1]),22))

    