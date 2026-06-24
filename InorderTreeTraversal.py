class tree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def inorder_traversal(root):
    if root is None:
        return []
    left = inorder_traversal(root.left)
    right = inorder_traversal(root.right)
    return left + [root.data] + right

tree_root = tree(1)
tree_root.left = tree(2)
tree_root.right = tree(3)
tree_root.left.left = tree(4)
print(inorder_traversal(tree_root))
