'''
863: All nodes distance K in Binary Tree
Given the root of a binary tree, the value of a target node target, and an integer k, 
return an array of the values of all nodes that have a distance k from the target node.
You can return the answer in any order.
e.g.
             3
          /     \
         5       1
       /  \     /  \
      6    2   0    8
          / \
         7   4    Target node 5 and k = 2, O/P => [1, 7, 4]
'''


from collections import defaultdict
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> list[int]:
        graph = defaultdict(list) # Adjacency list
        def build_graph(cur, parent):
            if cur and parent:
                graph[cur.val].append(parent.val)
                graph[parent.val].append(cur.val)
            if cur.left:
                build_graph(cur.left, cur)
            if cur.right:
                build_graph(cur.right, cur)
        build_graph(root, None)
        answer = []
        visited_nodes = set([target.val])
        queue = deque()
        queue.append((target.val, 0))
        while queue:
            node, distance = queue.popleft()
            if distance == k:
                answer.append(node)
                continue # No need to traverse neighbors
            for neighbor in graph[node]:
                if not neighbor in visited_nodes:
                    queue.append((neighbor, distance + 1)) 
                    visited_nodes.add(neighbor)      
        return answer
    
    def distanceKDFS(self, root: TreeNode, target: TreeNode, k: int) -> list[int]:
        graph = defaultdict(list) # Adjacency list
        visited_nodes = set([target.val])
        answer = []
        def build_graph(cur, parent):
            if cur and parent:
                graph[cur.val].append(parent.val)
                graph[parent.val].append(cur.val)
            if cur.left:
                build_graph(cur.left, cur)
            if cur.right:
                build_graph(cur.right, cur)
        def dfs(node, distance):
            nonlocal k
            if distance == k:
                answer.append(node)
                return
            for neighbor in graph[node]:
                if not neighbor in visited_nodes:
                    visited_nodes.add(neighbor)
                    dfs(neighbor, distance + 1)
        build_graph(root, None)
        dfs(target.val, 0)
        return answer
            


    
    def _create_tree(self, arr, target_val):
        if not arr:
            return None
        root = TreeNode(arr[0])
        n = len(arr)
        q = [root]
        i = 1
        target = None if root.val != target_val else root
        while i < n:
            node = q.pop(0)
            if node.val == target_val:
                target = node
            if arr[i] is not None:
                node.left = TreeNode(arr[i])
                q.append(node.left)
            i += 1
            if arr[i] is not None and i < n:
                node.right = TreeNode(arr[i])
                q.append(node.right)
            i += 1
        return [root, target]

    
sol = Solution()
arr = [3,5,1,6,2,0,8,None,None,7,4]
root, target = sol._create_tree(arr, 5)
print (sol.distanceK(root, target, 2))
print (sol.distanceKDFS(root, target, 2))


arr = [1]
root, target = sol._create_tree(arr, 1)
print (sol.distanceK(root, target, 3))
print (sol.distanceKDFS(root, target, 3))
            
            