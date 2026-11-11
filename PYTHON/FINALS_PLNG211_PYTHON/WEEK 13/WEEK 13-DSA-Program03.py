#WEEK 13-DSA-Program03.py
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

def count_nodes(root):
    if root is None:
        return 0
    return 1 + count_nodes(root.left) + count_nodes(root.right)

def count_leaves(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 1
    return count_leaves(root.left) + count_leaves(root.right)

def height(root):
    if root is None:
        return 0
    return 1 + max(height(root.left), height(root.right))

def read_values():
    while True:
        user_input = input("Enter space-separated integers (Press Enter for empty tree): ").strip()
        if not user_input:
            return []
        
        tokens = user_input.split()
        if len(tokens) > 100:
            print("Error: Input limit is 100 values. Please try again.")
            continue
        try:
            values = [int(tok) for tok in tokens]
            return values
        except ValueError:
            print("Invalid input detected! Please enter valid integers only.")

if __name__ == "__main__":
    input_values = read_values()
    bst_root = build_bst(input_values)

    print("Preorder  :", preorder(bst_root))
    print("Inorder   :", inorder(bst_root))
    print("Postorder :", postorder(bst_root))

    print("Unique Nodes :", count_nodes(bst_root))
    print("Leaf Nodes   :", count_leaves(bst_root))
    print("Tree Height  :", height(bst_root))