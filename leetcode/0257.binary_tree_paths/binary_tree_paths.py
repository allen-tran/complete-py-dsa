def binaryTreePaths(self, root):
    res = []
    self.dfs(res, root, "")
    return res


def dfs(self, res, node, string):
    if not node:
        return
    string += str(node.val)
    self.dfs(res, node.left, string+"->")
    self.dfs(res, node.right, string + "->")

    if not node.right and not node.left:
        res.append(string)
