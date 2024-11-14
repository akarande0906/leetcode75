from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right    

class Solution:
    def lca(self, root: TreeNode, nodes: list[TreeNode]) -> TreeNode:
        node_set = set(nodes)
        def helper(root):
            if root is None:
                return None
            if root.val in node_set:
                return root

            left = helper(root.left)
            right = helper(root.right)

            if left:
                print ('Left: ' + str(left.val))
            if right:
                print ('Right: ' + str(right.val))


            if left and right:
                return root
            return left if left else right
        return helper(root)

def createTree(arr):
    if not arr:
        return None
    q = deque()
    root = TreeNode(arr[0])
    q.append(root)
    n = 1
    while q and n < len(arr):
        node = q.popleft()
        if arr[n]:
            left = TreeNode(arr[n])
            node.left = left
            q.append(left)
        n += 1
        if arr[n]:
            right = TreeNode(arr[n])
            node.right = right
            q.append(right)
        n += 1
    return root


arr = [1,2,3,4,5,6,None,None,None,7,8,9,10]
print(Solution().lca(createTree(arr), [2,10]).val)
arr = [8,10,14,22,23,None,15,26,None,None,None,None,None,17,16]
print(Solution().lca(createTree(arr), [26,23]).val)
print(Solution().lca(createTree(arr), [22,16]).val)
arr = [3,5,1,6,2,0,8,None,None,7,4]
print(Solution().lca(createTree(arr), [1]).val)
print(Solution().lca(createTree(arr), [7,6,2,4]).val)
