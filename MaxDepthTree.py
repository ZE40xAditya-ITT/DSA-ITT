class Tree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def max_depth_tree(root):
    if root is None:
        return 0
    left_height = max_depth_tree(root.left)
    right_height = max_depth_tree(root.right)
    return 1 + max(left_height, right_height)

tree_root = Tree(1)
tree_root.left = Tree(2)
tree_root.right = Tree(3)
tree_root.left.left = Tree(4)
print(max_depth_tree(tree_root))