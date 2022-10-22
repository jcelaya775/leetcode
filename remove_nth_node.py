# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# input = [1, 2, 3, 4, 5]
# n = 2
# output = [1, 2, 3, 5]
# input = [1]
# n = 1
# output = []
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        end = head
        count = 1
        while end and count <= n:
            end = end.next
            count += 1
            
        nodeToRemove = head
        while end and end.next:
            nodeToRemove = nodeToRemove.next
            end = end.next
            
        if nodeToRemove:
            removeNode(nodeToRemove)
        return head

            
def removeNode(node):
    if node and node.next:
        node.next = node.next.next


def printLinkedList(head):
    curr = head
    while curr:
        print(curr.val)
        curr = curr.next


def main():
    input = Node(1, Node(2, Node(3, Node(4, Node(5, None)))))
    print(input)