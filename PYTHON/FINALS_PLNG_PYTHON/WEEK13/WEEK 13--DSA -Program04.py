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


def sum_nodes(root):
    if root is None:
        return 0

    return root.value + sum_nodes(root.left) + sum_nodes(root.right)


# Get numbers from the user
while True:
    try:
        numbers = input("Enter numbers separated by spaces: ").split()

        if len(numbers) == 0:
            print("Error! Please enter at least one number.")
            continue

        numbers = [int(num) for num in numbers]
        break

    except ValueError:
        print("Invalid input! Please enter integers only.")


root = None

for num in numbers:
    root = insert(root, num)


# Display full tree
print("\nFull tree")
print("Preorder:", preorder(root))
print("Inorder:", inorder(root))
print("Postorder:", postorder(root))


# Search for a value
while True:
    try:
        key = int(input("\nEnter number to search: "))
        break

    except ValueError:
        print("Invalid input! Please enter an integer.")


# Display selected subtree
result = search(root, key)

if result is not None:
    print("\nSubtree rooted at", key)
    print("Preorder:", preorder(result))
    print("Inorder:", inorder(result))
    print("Postorder:", postorder(result))
    print("Subtree node count:", count_nodes(result))
    print("Subtree sum:", sum_nodes(result))

else:
    print("Value not found!")
