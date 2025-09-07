class Codec:
    def serialize(self, root):
        if not root:
            return ""
        queue = [root]
        result = []
        while queue:
            node = queue.pop(0)
            if node:
                result.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append("#")
        return ",".join(result)

    def deserialize(self, data):
        if not data:
            return None
        values = data.split(",")
        root = TreeNode(int(values[0]))
        queue = [root]
        i = 1
        while queue:
            node = queue.pop(0)
            if values[i] != "#":
                left = TreeNode(int(values[i]))
                node.left = left
                queue.append(left)
            i += 1
            if values[i] != "#":
                right = TreeNode(int(values[i]))
                node.right = right
                queue.append(right)
            i += 1
        return root
