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


# Get user input
while True:
    try:
        numbers = input("Enter numbers separated by spaces: ").split()
        numbers = [int(num) for num in numbers]
        break

    except ValueError:
        print("Invalid input! Please enter integers only.")


root = None

for num in numbers:
    root = insert(root, num)


# Display results
print("\nPreorder:", preorder(root))
print("Inorder:", inorder(root))
print("Postorder:", postorder(root))

print("Unique nodes:", count_nodes(root))
print("Leaf nodes:", count_leaves(root))
print("Height:", height(root))
