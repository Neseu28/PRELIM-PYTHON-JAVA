
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


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


# get numbers from the user
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


# Create the binary tree
nodes = [Node(num) for num in numbers]

for i in range(len(nodes)):
    left = 2 * i + 1
    right = 2 * i + 2

    if left < len(nodes):
        nodes[i].left = nodes[left]

    if right < len(nodes):
        nodes[i].right = nodes[right]

root = nodes[0]


# display traversals
print("\nPreorder:", preorder(root))
print("Inorder:", inorder(root))
print("Postorder:", postorder(root))
