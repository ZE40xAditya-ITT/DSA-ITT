class tree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def postorder_traversal(root):
    if root is None:
        return []
    left = postorder_traversal(root.left)
    right = postorder_traversal(root.right)
    return left + right + [root.data]

tree_root = tree(1)
tree_root.left = tree(2)
tree_root.right = tree(3)
tree_root.left.left = tree(4)
print(postorder_traversal(tree_root))
