#WEEK 13-DSA-Program04.py

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

def search(root, key):
    if root is None or root.value == key:
        return root
    if key < root.value:
        return search(root.left, key)
    return search(root.right, key)


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

def subtree_sum(root):
    if root is None:
        return 0
    return root.value + subtree_sum(root.left) + subtree_sum(root.right)

if __name__ == "__main__":
    values = [50, 30, 70, 20, 40, 60, 80, 35, 45]
    root = build_bst(values)

    print("Full Tree Preorder :", preorder(root))
    print("Full Tree Inorder  :", inorder(root))
    
    user_key_input = input("\nEnter search key: ").strip()
    try:
        search_key = int(user_key_input)
        target_node = search(root, search_key)

        if target_node:
            print(f"\n--- Subtree Rooted at {search_key} ---")
            print("Subtree Preorder  :", preorder(target_node))
            print("Subtree Inorder   :", inorder(target_node))
            print("Subtree Postorder :", postorder(target_node))
            print("Subtree Node Count:", count_nodes(target_node))
            print("Subtree Value Sum :", subtree_sum(target_node))
        else:
            print("Value not found")
    except ValueError:
        print("Invalid search key! Please enter an integer.")