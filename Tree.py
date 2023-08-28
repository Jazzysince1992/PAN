class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

# In-order traversal (Left-Root-Right)
def in_order_traversal(node):
    if node:
        in_order_traversal(node.left)
        print(node.val, end=" ")
        in_order_traversal(node.right)

# Pre-order traversal (Root-Left-Right)
def pre_order_traversal(node):
    if node:
        print(node.val, end=" ")
        pre_order_traversal(node.left)
        pre_order_traversal(node.right)

# Post-order traversal (Left-Right-Root)
def post_order_traversal(node):
    if node:
        post_order_traversal(node.left)
        post_order_traversal(node.right)
        print(node.val, end=" ")

# Create the binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print("In-order traversal:")
in_order_traversal(root)
print("\n")

print("Pre-order traversal:")
pre_order_traversal(root)
print("\n")

print("Post-order traversal:")
post_order_traversal(root)
print("\n")
