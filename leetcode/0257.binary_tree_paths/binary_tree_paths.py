class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def binaryTreePaths(self, root):
        res = []
        self.dfs(res, root, "")

        return res

    def dfs(self, res, node, string):
        if not node:
            return

        string += str(node.val)

        if not node.left and not node.right:
            res.append(string)
        else:
            string += '->'
            self.dfs(res, node.left, string)
            self.dfs(res, node.right, string)


if __name__ == "__main__":
    root = Node(10)
    s = Solution()
    print(s.binaryTreePaths(root))
