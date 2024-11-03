# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

'''
    3
   / \
  9  20
    /  \
   15   7
'''

class Solution():
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        else:
            return max(self.maxDepth(root.left) + 1, self.maxDepth(root.right) + 1)
        

''' Alternative: BFS
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        else:
            # return max(self.maxDepth(root.left) + 1, self.maxDepth(root.right) + 1)
            bfs_queue = deque()
            bfs_queue.append((root, 1))
            while bfs_queue:
                root, depth = bfs_queue.popleft()
                print (root.val)
                if root.left:
                    bfs_queue.append((root.left, depth + 1))
                if root.right:
                    bfs_queue.append((root.right, depth + 1))
            return depth

'''
