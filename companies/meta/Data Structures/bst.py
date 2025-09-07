'''
Implemenet a Binary Search Tree
'''

class TreeNode:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None
    
class BST:
    def __init__(self):
        self.root = None

    def _insert_iterator_(self, cur, val):
        if not cur:
            return TreeNode(val)
        if cur.value < val: # Go right
            cur.right = self._insert_iterator_(cur.right, val)
        elif cur.value > val: # Go left
            cur.left = self._insert_iterator_(cur.left, val)
        return cur

    def insert(self, val):  
        if not self.root:
            self.root = TreeNode(val)
        else:
            cur = self.root
            self._insert_iterator_(cur, val)

    def _inorder_traversal_helper_(self, node):
        if not node:
            return
        else:
            if node.left: 
                self._inorder_traversal_helper_(node.left)
            print (node.value)
            if node.right:
                self._inorder_traversal_helper_(node.right)

    def inorder_iteration(self):
        if not self.root:
            return
        else:
            self._inorder_traversal_helper_(self.root)
    
    def _findMinValueNode_(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current
        

    def _delete_iterator_(self, node, val):
        if not node:
            return None
        else:
            if val < node.value:
                node.left =  self._delete_iterator_(node.left, val)
            elif val > node.value:
                node.right = self._delete_iterator_(node.right, val)
            else: # This is the node to delete
                if not node.left:
                    temp_node = node.right
                    node = None
                    return temp_node
                elif not node.right:
                    temp_node = node.left
                    node = None
                    return temp_node
                else: # Both children are present. Get the successor node
                    temp_node = self._findMinValueNode_(node.right)
                    node.value = temp_node.value
                    node.right = self._delete_iterator_(node.right, temp_node.value)
                    
            return node

    def delete(self, val):
        if not self.root:
            return False
        else:
            return self._delete_iterator_(self.root, val)

    

# Create BST
bst = BST()
bst.insert(8)
bst.insert(3)
bst.insert(1)
bst.insert(6)
bst.insert(7)
bst.insert(10)
bst.insert(14)
bst.insert(4)
bst.inorder_iteration()
bst.delete(10)
bst.delete(10)
bst.inorder_iteration()

        
        
        

