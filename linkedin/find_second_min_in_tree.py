# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# LC: 671
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
            firstMin = secondMin = float('inf')
            def findSecondMin(root):
                nonlocal firstMin, secondMin
                if root is None:
                    return
                if root.val < firstMin:
                    secondMin = firstMin
                    firstMin = root.val
                elif firstMin < root.val < secondMin:
                    secondMin = root.val
                findSecondMin(root.left)
                findSecondMin(root.right)
            findSecondMin(root)
            return secondMin if secondMin != float('inf') else -1
