class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def inorderTraversal(self, root):
        tree_vals = []

        def inorder(node):
            if not node:
                return
            inorder(node.left)
            tree_vals.append(node.val)
            inorder(node.right)

        inorder(root)
        return tree_vals


if __name__ == "__main__":
    s = Solution()

    root = Node(10)
    root.left = Node(8)
    root.right = Node(16)
    print(s.inorderTraversal(root))
