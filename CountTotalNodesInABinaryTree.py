class Tree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def count_nodes(root):
    if root is None:
        return 0
    
    left_count = count_nodes(root.left)
    right_count = count_nodes(root.right)
    return 1 + left_count + right_count

tree_root = Tree(1)
tree_root.left = Tree(2)
tree_root.right = Tree(3)
tree_root.left.left = Tree(4)
tree_root.left.right = Tree(5)
print(count_nodes(tree_root))