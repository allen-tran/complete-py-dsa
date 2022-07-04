def inorderTraversal(root):
    tree_vals = []

    def inorder(node):
        if not node:
            return
        inorder(node.left)
        tree_vals.append(node.val)
        inorder(node.right)

    inorder(root)
    return tree_vals
