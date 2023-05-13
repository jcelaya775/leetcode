class Node:
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def printNode(self):
        print(f"Value: {self.value}, Prev: {self.left}, Next: {self.right}")


class BinaryTree:
    def __init__(self, root=None):
        self.root = root

    def binarySearch(self, value):
        curr = self.root

        while curr:
            if value == curr.value:
                print(f"{value} found!")
                return curr
            elif value >= curr.value:
                curr = curr.right
            else:
                curr = curr.left

        print(f"{value} not found...")
        return None

    def recursiveInorderTraversal(self, node):
        if not node:
            return

        self.recursiveInorderTraversal(node.left)
        print(node.value, end=" ")
        self.recursiveInorderTraversal(node.right)

    def iterativeInorderTraversal(self):
        node = self.root
        stack = []

        while True:
            if node:
                stack.append(node)
                node = node.left
            elif stack:
                node = stack.pop()
                print(node.value, end=" ")
                node = node.right
            else:  # no nodes left
                break

    def recursivePreorderTraversal(self, node):
        if node:
            print(node.value, end=" ")
            self.recursivePreorderTraversal(node.left)
            self.recursivePreorderTraversal(node.right)

    def recursivePostorderTraversal(self, node):
        if not node:
            return

        self.recursivePostorderTraversal(node.left)
        self.recursivePostorderTraversal(node.right)
        print(node.value, end=" ")


def main():
    bt = BinaryTree()

    # intialize binary tree
    root = Node(10)
    one = Node(5, Node(1), Node(7))
    root.left = one
    two = Node(15, Node(12), Node(17))
    root.right = two

    bt.root = root

    # traverse and search tree
    print("inorder:")
    bt.recursiveInorderTraversal(bt.root)
    print()
    bt.iterativeInorderTraversal()
    print("\npreorder:")
    bt.recursivePreorderTraversal(bt.root)
    print("\npostorder:")
    bt.recursivePostorderTraversal(bt.root)
    print()


main()
