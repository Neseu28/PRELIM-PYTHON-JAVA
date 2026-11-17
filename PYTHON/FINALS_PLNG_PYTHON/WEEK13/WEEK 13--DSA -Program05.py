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


def mirror_copy(root):
    if root is None:
        return None

    new_node = Node(root.value)

    new_node.left = mirror_copy(root.right)
    new_node.right = mirror_copy(root.left)

    return new_node


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


# Build the original BST
root = None

for num in numbers:
    root = insert(root, num)


# Save original traversals
original_preorder = preorder(root)
original_inorder = inorder(root)
original_postorder = postorder(root)


# Display original tree
print("\nOriginal tree")
print("Preorder:", original_preorder)
print("Inorder:", original_inorder)
print("Postorder:", original_postorder)


# Create mirrored tree
mirrored = mirror_copy(root)


# Display mirrored tree
print("\nMirrored tree")
print("Preorder:", preorder(mirrored))
print("Inorder:", inorder(mirrored))
print("Postorder:", postorder(mirrored))


# Compare traversals
print("\nInorder reversed:",
      inorder(mirrored) == original_inorder[::-1])

print("Original unchanged:",
      preorder(root) == original_preorder and
      inorder(root) == original_inorder and
      postorder(root) == original_postorder)
