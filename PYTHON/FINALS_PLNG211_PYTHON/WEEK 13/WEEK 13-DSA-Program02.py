#WEEK 13-DSA-Program02.py

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def insert(root, value):
    if root is None:
        return Node(value)
    if value < root.value:
        root.left = insert(root.left, value)
    elif value > root.value:
        root.right = insert(root.right, value)
    return root

def build_bst(values):
    if not values:
        return None
    root = None
    for val in values:
        root = insert(root, val)
    return root

def preorder(root):
    if root is None:
        return []
    return [root.value] + preorder(root.left) + preorder(root.right)

def inorder(root):
    if root is None:
        return []
    return inorder(root.left) + [root.value] + inorder(root.right)

def postorder(root):
    if root is None:
        return []
    return postorder(root.left) + postorder(root.right) + [root.value]

if __name__ == "__main__":
    insertion_list = [50, 30, 70, 20, 40, 60, 80, 30]
    bst_root = build_bst(insertion_list)

    print("Original Insertion List :", insertion_list)
    print("Preorder Traversal      :", preorder(bst_root))
    print("Inorder Traversal       :", inorder(bst_root))
    print("Postorder Traversal     :", postorder(bst_root))
