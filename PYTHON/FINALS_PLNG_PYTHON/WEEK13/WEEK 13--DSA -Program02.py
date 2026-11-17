
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


# Get user input
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


# Display results
print("\nInsertion list:", numbers)
print("Preorder:", preorder(root))
print("Inorder:", inorder(root))
print("Postorder:", postorder(root))
