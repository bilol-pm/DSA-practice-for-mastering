from collections import deque


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

root = Node(1)
root.left = Node(2)
root.right = Node(3)

def inorder_traversal(node):
    if node is not None:
        inorder_traversal(node.left)
        print(node.value)
        inorder_traversal(node.right)

def preorder_traversal(node):
    if node is not None:
        print(node.value)
        preorder_traversal(node.left)
        preorder_traversal(node.right)

def postorder_traversal(node):
    if node is not None:
        postorder_traversal(node.left)
        postorder_traversal(node.right)
        print(node.value)

def bfs_traversal(root):
    if root is None:
        return
    queue = deque([root])

    while queue:
        node = queue.popleft()
        print(node.value, end=" ")
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)







print("Result of inorder_traversal: ")
inorder_traversal(root)
print("Result of preorder_traversal: ")
preorder_traversal(root)
print("Result of postorder_traversal: ")
postorder_traversal(root)

print("Root:", root.value)
print("Left:", root.left.value)
print("Right:", root.right.value)
print("BFS: ")
bfs_traversal(root)