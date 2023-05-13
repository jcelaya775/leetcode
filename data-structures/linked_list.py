class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def length(self):
        length = 0
        while self.head:
            head = head.next
            length += 1
        return length

    def insertAfter(self, node, insertAfterNode):
        node.next = insertAfterNode.next
        node.prev = insertAfterNode
        insertAfterNode.next.prev = node
        insertAfterNode.next = node

    def get(self, index):
        curr = self.head
        i = 0
        while curr and i < index:
            curr = curr.next
            i += 1
        return curr.val

    def listToNode(self, arr):
        if len(arr) == 0:
            return

        self.head = None
        prev = None
        for num in arr:
            newNode = Node(num)
            if not self.head:
                self.head = newNode
            newNode.prev = prev
            if prev:
                prev.next = newNode
            prev = newNode

    def printLinkedList(self):
        curr = self.head
        while curr:
            print(curr.value, end=" -> ")
            curr = curr.next
        print("None")


class Node:
    def __init__(self, value=None, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    def printNode(self):
        print(f"Value: {self.value}, Prev: {self.prev}, Next: {self.next}")


def main():
    # initialize linked list
    arr = [1, 2, 3, 4, 5, 6, 76]
    linked = LinkedList()
    linked.listToNode(arr)
    linked.printLinkedList()

    head = linked.head
    curr = head
    while curr:
        curr = curr.next


main()
