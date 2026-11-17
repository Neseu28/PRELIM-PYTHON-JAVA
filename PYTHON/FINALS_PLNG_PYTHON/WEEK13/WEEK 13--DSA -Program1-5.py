class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# COMMON FUNCTIONS

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


def get_numbers():
    while True:
        try:
            numbers = input("Enter numbers separated by spaces: ").split()

            numbers = [int(num) for num in numbers]

            return numbers

        except ValueError:
            print("Invalid input! Please enter integers only.")


def get_search_value():
    while True:
        try:
            return int(input("Enter number to search: "))

        except ValueError:
            print("Invalid input! Please enter an integer.")



# BST FUNCTIONS 

def insert(root, value):
    if root is None:
        return Node(value)

    if value < root.value:
        root.left = insert(root.left, value)

    elif value > root.value:
        root.right = insert(root.right, value)

    return root


def build_bst(numbers):
    root = None

    for num in numbers:
        root = insert(root, num)

    return root


# PROGRAM 1 - TRAVERSE A GIVEN BINARY TREE

def program1():
    print("\n===== PROGRAM 1: BINARY TREE TRAVERSAL =====")

    numbers = get_numbers()

    if len(numbers) == 0:
        print("No numbers entered!")
        return

    nodes = [Node(num) for num in numbers]

    for i in range(len(nodes)):
        left = 2 * i + 1
        right = 2 * i + 2

        if left < len(nodes):
            nodes[i].left = nodes[left]

        if right < len(nodes):
            nodes[i].right = nodes[right]

    root = nodes[0]

    print("\nPreorder:", preorder(root))
    print("Inorder:", inorder(root))
    print("Postorder:", postorder(root))


# PROGRAM 2 - BUILD AND TRAVERSE BST


def program2():
    print("\n===== PROGRAM 2: BUILD AND TRAVERSE BST =====")

    numbers = get_numbers()

    if len(numbers) == 0:
        print("No numbers entered!")
        return

    root = build_bst(numbers)

    print("\nInsertion list:", numbers)
    print("Preorder:", preorder(root))
    print("Inorder:", inorder(root))
    print("Postorder:", postorder(root))



# PROGRAM 3 - ANALYZE A SEARCH TREE


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


def program3():
    print("\n===== PROGRAM 3: ANALYZE A SEARCH TREE =====")

    numbers = get_numbers()

    root = build_bst(numbers)

    print("\nPreorder:", preorder(root))
    print("Inorder:", inorder(root))
    print("Postorder:", postorder(root))

    print("Unique nodes:", count_nodes(root))
    print("Leaf nodes:", count_leaves(root))
    print("Height:", height(root))



# PROGRAM 4 - SEARCH AND TRAVERSE SUBTREE


def search(root, key):
    if root is None or root.value == key:
        return root

    if key < root.value:
        return search(root.left, key)

    return search(root.right, key)


def sum_nodes(root):
    if root is None:
        return 0

    return root.value + sum_nodes(root.left) + sum_nodes(root.right)


def program4():
    print("\n===== PROGRAM 4: SEARCH AND TRAVERSE SUBTREE =====")

    numbers = get_numbers()

    if len(numbers) == 0:
        print("No numbers entered!")
        return

    root = build_bst(numbers)

    print("\nFull tree")
    print("Preorder:", preorder(root))
    print("Inorder:", inorder(root))
    print("Postorder:", postorder(root))

    key = get_search_value()

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


# PROGRAM 5 - MIRROR A TREE


def mirror_copy(root):
    if root is None:
        return None

    new_node = Node(root.value)

    new_node.left = mirror_copy(root.right)
    new_node.right = mirror_copy(root.left)

    return new_node


def program5():
    print("\n===== PROGRAM 5: MIRROR A TREE =====")

    numbers = get_numbers()

    if len(numbers) == 0:
        print("No numbers entered!")
        return

    root = build_bst(numbers)

    # Save original traversals
    original_preorder = preorder(root)
    original_inorder = inorder(root)
    original_postorder = postorder(root)

    print("\nOriginal tree")
    print("Preorder:", original_preorder)
    print("Inorder:", original_inorder)
    print("Postorder:", original_postorder)

    # Create mirrored copy
    mirrored = mirror_copy(root)

    print("\nMirrored tree")
    print("Preorder:", preorder(mirrored))
    print("Inorder:", inorder(mirrored))
    print("Postorder:", postorder(mirrored))

    # Compare results
    print("\nInorder reversed:",
          inorder(mirrored) == original_inorder[::-1])

    print("Original unchanged:",
          preorder(root) == original_preorder and
          inorder(root) == original_inorder and
          postorder(root) == original_postorder)


# ==============================
# MAIN MENU
# ==============================

while True:

    print("\n===================================")
    print("       BINARY TREE ACTIVITIES")
    print("===================================")
    print("[1] Traverse a Given Binary Tree")
    print("[2] Build and Traverse a BST")
    print("[3] Analyze a Search Tree")
    print("[4] Search and Traverse a Subtree")
    print("[5] Mirror a Tree and Compare")
    print("[0] Exit")
    print("===================================")

    choice = input("Choose a program (0-5): ").strip()

    if choice == "1":
        program1()

    elif choice == "2":
        program2()

    elif choice == "3":
        program3()

    elif choice == "4":
        program4()

    elif choice == "5":
        program5()

    elif choice == "0":
        print("\nThank you for using the program!")
        break

    else:
        print("\nInvalid choice! Please select from 0 to 5.")
